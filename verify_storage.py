import os
import django
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from dotenv import load_dotenv

# Force load env first just in case
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

def check_storage():
    print(f"DEBUG: Cloud Name from env: {os.getenv('CLOUDINARY_CLOUD_NAME')}")
    print(f"DEBUG: DEFAULT_FILE_STORAGE setting: {settings.DEFAULT_FILE_STORAGE}")
    
    file_name = 'test_cloudinary_verify_v2.txt'
    file_content = b'Verifying Cloudinary v2'
    
    try:
        print("Attempting to save file...")
        saved_name = default_storage.save(file_name, ContentFile(file_content))
        print(f"Saved file name: {saved_name}")
        
        file_url = default_storage.url(saved_name)
        print(f"File URL: {file_url}")
        
        if 'cloudinary' in file_url:
            print("SUCCESS: Cloudinary is working!")
        else:
            print("FAIL: URL suggests local storage.")
            
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_storage()
