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
    'Biographies', 'Academic', 'Self-Help', 'Exams (UPSC/JEE)', 'Romance'
]

cats = {}
for name in categories_data:
    cat, _ = Category.objects.get_or_create(name=name)
    cats[name] = cat
    # print(f"Category: {name}")

# Expanded Book List
books_data = [
    # Fiction
    ("The Midnight Library", "Matt Haig", "Fiction", 499),
    ("It Ends With Us", "Colleen Hoover", "Fiction", 299),
    ("The Alchemist", "Paulo Coelho", "Fiction", 290),
    ("The Kite Runner", "Khaled Hosseini", "Fiction", 399),
    ("A Thousand Splendid Suns", "Khaled Hosseini", "Fiction", 420),
    
    # Business
    ("The Psychology of Money", "Morgan Housel", "Business & Management", 399),
    ("Rich Dad Poor Dad", "Robert Kiyosaki", "Business & Management", 350),
    ("Deep Work", "Cal Newport", "Business & Management", 410),
    ("Good to Great", "Jim Collins", "Business & Management", 480),
    ("Zero to One", "Peter Thiel", "Business & Management", 510),
    ("Atomic Habits", "James Clear", "Self-Help", 550),

    # Crime & Thriller
    ("The Silent Patient", "Alex Michaelides", "Crime, Thriller & Mystery", 320),
    ("Gone Girl", "Gillian Flynn", "Crime, Thriller & Mystery", 350),
    ("The Girl on the Train", "Paula Hawkins", "Crime, Thriller & Mystery", 299),

    # Children
    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Children & Young Adult", 450),
    ("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Children & Young Adult", 499),
    ("Percy Jackson: The Lightning Thief", "Rick Riordan", "Children & Young Adult", 399),
    
    # Bio
    ("Wings of Fire", "A.P.J. Abdul Kalam", "Biographies", 250),
    ("Educated", "Tara Westover", "Biographies", 420),
    ("Steve Jobs", "Walter Isaacson", "Biographies", 600),

    # Non-Fiction
    ("Sapiens", "Yuval Noah Harari", "Non-Fiction", 600),
    ("Thinking, Fast and Slow", "Daniel Kahneman", "Non-Fiction", 550),
    ("Ikigai", "Hector Garcia", "Self-Help", 350),

    # Academic/Exams
    ("Indian Polity", "M. Laxmikanth", "Exams (UPSC/JEE)", 750),
    ("Concept of Physics Vol 1", "H.C. Verma", "Exams (UPSC/JEE)", 450),
    ("NCERT Mathematics Class 12", "NCERT", "Exams (UPSC/JEE)", 150),
]

# Create Books
print("Adding books...")
count = 0
for title, author, cat_name, price in books_data:
    if not Book.objects.filter(title=title).exists():
        Book.objects.create(
            title=title,
            author=author,
            category=cats[cat_name],
            description=f"A highly rated book by {author}. This copy is in excellent condition and ready for a new home. Essential reading for fans of {cat_name}.",
            price=price,
            condition=random.choice(['New', 'Like New', 'Good']),
            seller=seller,
            status='Approved'
        )
        print(f" + Added: {title}")
        count += 1
    else:
        print(f" . Skipped (Exists): {title}")

print(f"Done! Added {count} new books.")
