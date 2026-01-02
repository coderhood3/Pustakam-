import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')

try:
    from django.core.management import execute_from_command_line
    print("Attempting validation...")
    execute_from_command_line(['manage.py', 'check'])
    print("Settings check passed.")
except Exception as e:
    import traceback
    traceback.print_exc()
