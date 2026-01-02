import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
password = 'admin123'

try:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print(f"SUCCESS: Password for '{username}' has been RESET to '{password}'.")
except User.DoesNotExist:
    print(f"User '{username}' does not exist. Creating now...")
    User.objects.create_superuser(username=username, email='admin@example.com', password=password)
    print(f"SUCCESS: Superuser '{username}' created with password '{password}'.")
