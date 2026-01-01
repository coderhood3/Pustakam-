import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

def debug_settings():
    print(f"DEBUG: DEFAULT_FILE_STORAGE = {getattr(settings, 'DEFAULT_FILE_STORAGE', 'NOT SET')}")
    print(f"DEBUG: STORAGES = {getattr(settings, 'STORAGES', 'NOT SET')}")
    print(f"DEBUG: DEBUG = {settings.DEBUG}")
    
    from django.core.files.storage import default_storage
    print(f"DEBUG: default_storage class = {default_storage.__class__}")
    print(f"DEBUG: default_storage module = {default_storage.__class__.__module__}")

if __name__ == "__main__":
    debug_settings()
