from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
author_name = "John Fred"  
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(book.title)
except Author.DoesNotExist:
    print("Author not found.")


# Query 2: List all books in a library
library_name = "Central Library"  
try:
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books:
        print(book.title)
except Library.DoesNotExist:
    print("Library not found.")


# Query 3: Retrieve the librarian for a library
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print("Librarian or Library not found.")
