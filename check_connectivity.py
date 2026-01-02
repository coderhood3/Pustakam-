import os
import django
import cloudinary
import cloudinary.uploader

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
from dotenv import load_dotenv
load_dotenv()
django.setup()

def check_cloudinary():
    print("Checking Cloudinary Connectivity...")
    try:
        # Simple ping by uploading a tiny data URI
        response = cloudinary.uploader.upload("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
        print(f"SUCCESS: Connected to Cloudinary! Uploaded test image.")
        print(f"Public ID: {response['public_id']}")
        print(f"URL: {response['secure_url']}")
        return True
    except Exception as e:
        print(f"ERROR: Cloudinary Connection Failed.")
        print(e)
        return False

if __name__ == "__main__":
    check_cloudinary()
