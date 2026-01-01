import os
import traceback

# Force production mode
os.environ['DEBUG'] = 'False'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')

try:
    import django
    from django.conf import settings
    django.setup()
    
    print("Settings loaded successfully.")
    print(f"DEBUG: {settings.DEBUG}")
    print(f"STATICFILES_DIRS: {getattr(settings, 'STATICFILES_DIRS', 'MISSING')}")
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    
except Exception:
    print("Caught exception during setup:")
    traceback.print_exc()
