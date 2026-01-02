import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

from django.contrib.auth import get_user_model
from books.models import Category, Book

User = get_user_model()

# Ensure a seller exists
seller, created = User.objects.get_or_create(username='pustakam_official', email='admin@pustakam.com')
if created:
    seller.set_password('admin123')
    seller.save()

# Categories
categories_data = [
    'Fiction', 'Non-Fiction', 'Business & Management', 
    'Children & Young Adult', 'Crime, Thriller & Mystery', 
    'Biographies', 'Academic', 'Self-Help'
]

cats = {}
for name in categories_data:
    cat, _ = Category.objects.get_or_create(name=name)
    cats[name] = cat
    print(f"Category: {name}")

# Sample Books Data
books_data = [
    ("The Midnight Library", "Matt Haig", "Fiction", 499),
    ("Atomic Habits", "James Clear", "Self-Help", 550),
    ("The Psychology of Money", "Morgan Housel", "Business & Management", 399),
    ("It Ends With Us", "Colleen Hoover", "Fiction", 299),
    ("Rich Dad Poor Dad", "Robert Kiyosaki", "Business & Management", 350),
    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Children & Young Adult", 450),
    ("The Silent Patient", "Alex Michaelides", "Crime, Thriller & Mystery", 320),
    ("Wings of Fire", "A.P.J. Abdul Kalam", "Biographies", 250),
    ("Sapiens", "Yuval Noah Harari", "Non-Fiction", 600),
    ("Project Hail Mary", "Andy Weir", "Fiction", 520),
    ("Deep Work", "Cal Newport", "Business & Management", 410),
    ("Good to Great", "Jim Collins", "Business & Management", 480),
    ("The Alchemist", "Paulo Coelho", "Fiction", 290),
    ("Educated", "Tara Westover", "Biographies", 420),
    ("Zero to One", "Peter Thiel", "Business & Management", 510),
]

# Create Books
for title, author, cat_name, price in books_data:
    if not Book.objects.filter(title=title).exists():
        Book.objects.create(
            title=title,
            author=author,
            category=cats[cat_name],
            description=f"A best-selling book by {author}. In excellent condition. Essential reading for everyone interested in {cat_name}.",
            price=price,
            condition='Like New',
            seller=seller,
            status='Approved'
        )
        print(f"Added Book: {title}")

print("Store populated successfully!")
