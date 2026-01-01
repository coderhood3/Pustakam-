import os
import django
from django.core.files import File

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

from books.models import Book
from django.conf import settings

def migrate_images():
    print("="*50)
    print("STARTING MEDIA MIGRATION TO CLOUDINARY")
    print("="*50)
    
    books = Book.objects.all()
    count = 0
    success_count = 0
    
    # Define local media root manually since settings.MEDIA_ROOT might be used by Cloudinary storage now
    # dependent on configuration. But usually BASE_DIR / 'media' is where user files are.
    local_media_root = settings.BASE_DIR / 'media'

    for book in books:
        if not book.image:
            continue
            
        count += 1
        # The DB currently holds the relative path, e.g. 'books/b1.jpg'
        db_path = str(book.image)
        
        # Check if this is already a full URL (already migrated?)
        if db_path.startswith('http'):
            print(f"[SKIP] Book '{book.title}' already seems to be a URL.")
            continue

        # Construct local path
        local_path = local_media_root / db_path
        
        print(f"Processing '{book.title}'...")
        print(f"  -> Path in DB: {db_path}")
        print(f"  -> Looking for: {local_path}")
        
        if os.path.exists(local_path):
            print(f"  -> Found local file. Uploading...")
            try:
                # Open the local file and save it back to the field.
                # This triggers the configured storage (Cloudinary) to upload it.
                with open(local_path, 'rb') as f:
                    # We use basename to ensure it goes into the correct folder structure 
                    # defined by upload_to in the model, usually.
                    filename = os.path.basename(db_path)
                    
                    # Passing save=True updates the DB instance
                    book.image.save(filename, File(f), save=True)
                    
                print(f"  -> SUCCESS: Uploaded as '{book.image.name}'")
                success_count += 1
            except Exception as e:
                print(f"  -> ERROR during upload: {e}")
        else:
            print(f"  -> WARNING: Local file not found at {local_path}")
            
    print("="*50)
    print(f"MIGRATION COMPLETE")
    print(f"Processed: {count}")
    print(f"Uploaded:  {success_count}")
    print("="*50)

if __name__ == '__main__':
    migrate_images()
