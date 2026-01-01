import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

from books.models import Book
from django.core.files.storage import default_storage

print(f"Default Storage Class: {default_storage.__class__.__name__}")
print(f"Settings DEFAULT_FILE_STORAGE: {getattr(settings, 'DEFAULT_FILE_STORAGE', 'Not Set')}")
try:
    print(f"Settings STORAGES: {getattr(settings, 'STORAGES', 'Not Set')}")
except Exception:
    pass

books = Book.objects.all()
if books.exists():
    book = books.first()
    print(f"Book Image Field Storage: {book.image.storage.__class__.__name__}")
    print(f"Image URL: {book.image.url}")
else:
    print("No books found.")
