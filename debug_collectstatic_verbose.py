import os
import sys
import traceback
from django.core.management import execute_from_command_line

# Force production mode
os.environ['DEBUG'] = 'False'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')

print("Debugging collectstatic failure...")
try:
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '-v', '3'])
    print("Collectstatic finished successfully.")
except Exception:
    print("Detailed Traceback:")
    traceback.print_exc()
