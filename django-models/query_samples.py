import os
import django

# Setup Django if running as standalone script (optional safety check)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query: All books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

# Query: All books in a specific library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

# Query: Retrieve librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian of {library_name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print(f"Librarian not found for {library_name}")

# Example usage (can be replaced with test data)
if __name__ == "__main__":
    query_books_by_author("John Doe")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
