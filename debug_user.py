import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'Robin'

try:
    user = User.objects.get(username=username)
    print(f"User: {user.username}")
    print(f"Active: {user.is_active}")
    print(f"Staff: {user.is_staff}")
    print(f"Superuser: {user.is_superuser}")
    print(f"Password Usable: {user.has_usable_password()}")
    # Attempt to authenticate programmatically
    from django.contrib.auth import authenticate
    # We can't know the password the user typed, but we can verify the user object state.
    
    print("-" * 20)
    # Check admin user too
    admin_user = User.objects.get(username='admin')
    print(f"User: {admin_user.username}")
    print(f"Active: {admin_user.is_active}")
    print(f"Staff: {admin_user.is_staff}")
    print(f"Superuser: {admin_user.is_superuser}")
    
except User.DoesNotExist:
    print(f"User '{username}' does not exist.")
except Exception as e:
    print(f"Error: {e}")
