import os
import django
from django.conf import settings
from django.core.files.storage import default_storage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

def debug_storage():
    print(f"DEBUG: Active Storage Class: {default_storage.__class__.__name__}")
    print(f"DEBUG: Storage Base URL: {getattr(default_storage, 'base_url', 'N/A')}")
    
    # Check what URL it generates for a simple string
    test_path = 'books/b1.jpg'
    url = default_storage.url(test_path)
    print(f"DEBUG: URL for '{test_path}': {url}")
    
    # Check if we can instantiate Cloudinary storage explicitly
    try:
        from cloudinary_storage.storage import MediaCloudinaryStorage
        cloud_storage = MediaCloudinaryStorage()
        print(f"DEBUG: Explicit Cloudinary URL: {cloud_storage.url(test_path)}")
    except Exception as e:
        print(f"DEBUG: Could not instantiate Cloudinary directly: {e}")

if __name__ == "__main__":
    debug_storage()
