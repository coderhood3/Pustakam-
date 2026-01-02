import os
import django
import random
from django.core.files import File
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pustakam.settings')
django.setup()

from django.contrib.auth import get_user_model
from books.models import Category, Book

User = get_user_model()
seller = User.objects.get(username='pustakam_official')

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


# Map categories to cover images
cover_map = {
    'Fiction': 'cover_fiction.png',
    'Crime, Thriller & Mystery': 'cover_thriller.png',
    'Children & Young Adult': 'cover_kids.png',
    'Business & Management': 'cover_business.png',
    'Self-Help': 'cover_business.png', # Reusing business for self-help
    'Non-Fiction': 'cover_business.png',
    'Biographies': 'cover_fiction.png',
    'Academic': 'cover_business.png',
    'Exams (UPSC/JEE)': 'cover_business.png'
}

# Expanded Book List
books_data = [
    ("The Midnight Library", "Matt Haig", "Fiction", 499),
    ("It Ends With Us", "Colleen Hoover", "Fiction", 299),
    ("The Alchemist", "Paulo Coelho", "Fiction", 290),
    ("The Kite Runner", "Khaled Hosseini", "Fiction", 399),
    ("A Thousand Splendid Suns", "Khaled Hosseini", "Fiction", 420),
    ("The Psychology of Money", "Morgan Housel", "Business & Management", 399),
    ("Rich Dad Poor Dad", "Robert Kiyosaki", "Business & Management", 350),
    ("Deep Work", "Cal Newport", "Business & Management", 410),
    ("Good to Great", "Jim Collins", "Business & Management", 480),
    ("Zero to One", "Peter Thiel", "Business & Management", 510),
    ("Atomic Habits", "James Clear", "Self-Help", 550),
    ("The Silent Patient", "Alex Michaelides", "Crime, Thriller & Mystery", 320),
    ("Gone Girl", "Gillian Flynn", "Crime, Thriller & Mystery", 350),
    ("The Girl on the Train", "Paula Hawkins", "Crime, Thriller & Mystery", 299),
    ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Children & Young Adult", 450),
    ("Harry Potter and the Chamber of Secrets", "J.K. Rowling", "Children & Young Adult", 499),
    ("Percy Jackson: The Lightning Thief", "Rick Riordan", "Children & Young Adult", 399),
    ("Wings of Fire", "A.P.J. Abdul Kalam", "Biographies", 250),
    ("Educated", "Tara Westover", "Biographies", 420),
    ("Steve Jobs", "Walter Isaacson", "Biographies", 600),
    ("Sapiens", "Yuval Noah Harari", "Non-Fiction", 600),
    ("Thinking, Fast and Slow", "Daniel Kahneman", "Non-Fiction", 550),
    ("Ikigai", "Hector Garcia", "Self-Help", 350),
    ("Indian Polity", "M. Laxmikanth", "Exams (UPSC/JEE)", 750),
    ("Concept of Physics Vol 1", "H.C. Verma", "Exams (UPSC/JEE)", 450),
    ("NCERT Mathematics Class 12", "NCERT", "Exams (UPSC/JEE)", 150),
]

# Path to static images (source for covers)
static_img_path = os.path.join(settings.BASE_DIR, 'static', 'books', 'images')

print("Updating books with Premium Covers...")
for title, author, cat_name, price in books_data:
    cover_filename = cover_map.get(cat_name, 'cover_fiction.png') # Default to fiction
    cover_src = os.path.join(static_img_path, cover_filename)
    
    # Check if book exists
    book_qs = Book.objects.filter(title=title)
    if book_qs.exists():
        book = book_qs.first()
        # If no image, assign one
        if not book.image and os.path.exists(cover_src):
            with open(cover_src, 'rb') as f:
                book.image.save(cover_filename, File(f), save=True)
            print(f"Updated Image: {title}")
    else:
        # Create new
        book = Book(
            title=title,
            author=author,
            category=cats[cat_name],
            description=f"A highly rated book by {author}. This copy is in excellent condition.",
            price=price,
            condition=random.choice(['New', 'Like New']),
            seller=seller,
            status='Approved'
        )
        if os.path.exists(cover_src):
            with open(cover_src, 'rb') as f:
                book.image.save(cover_filename, File(f), save=False)
        book.save()
        print(f"Created Book: {title}")

print("Premium Upgrade Complete!")
