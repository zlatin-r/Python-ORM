import os
import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Customer, Book

# Create queries within functions

# Task 1:
# customer = Customer(
#     name="Svetlin Nakov1",
#     age=1,
#     email="nakov@example",
#     phone_number="+35912345678",
#     website_url="htsatps://nakov.com/")
# try:
#     customer.full_clean()
#     customer.save()
# except ValidationError as e:
#     print('\n'.join(e.messages))
# ---------------------------------------------------------------
# Task 2:
# book = Book(
#     title="Short Title",
#     description="A book with a short title.",
#     genre="Fiction",
#     author="A",
#     isbn="1234")
#
# try:
#     book.full_clean()
#     book.save()
# except ValidationError as e:
#     print("Validation Error for Book:")
#
#     for field, errors in e.message_dict.items():
#         print(f"{field}: {', '.join(errors)}")
# -----------------------------------------------------
# Task 3:
