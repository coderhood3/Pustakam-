import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
email = 'admin@pustakam.com'
password = 'admin123'

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser: {username}")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully!")
else:
    print(f"Superuser '{username}' already exists.")
    
# Also ensure pustakam_official is staff/superuser if needed, or just leave it. 
# Let's just focus on the 'admin' user for the admin panel access.
