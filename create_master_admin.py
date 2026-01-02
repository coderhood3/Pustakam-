import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'master'
password = 'password123'

try:
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        user.delete()
        print(f"Deleted old '{username}' user.")

    User.objects.create_superuser(username=username, email='master@example.com', password=password)
    print(f"SUCCESS: Created NEW superuser '{username}' with password '{password}'")
    
except Exception as e:
    print(f"Error: {e}")
