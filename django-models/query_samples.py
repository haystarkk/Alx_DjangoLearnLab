from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Fred Connor"  
authors = Author.objects.filter(name=author_name)
if authors.exists():
    author = authors.first()
    books = Book.objects.filter(author=author)
    for book in books:
        print(book.title)
else:
    print("Author not found.")

# List all books in a library
library_name = "Central Library"  
libraries = Library.objects.filter(name=library_name)
if libraries.exists():
    library = libraries.first()
    books = library.books.all()
    for book in books:
        print(book.title)
else:
    print("Library not found.")

# Retrieve the librarian for a library
if libraries.exists():
    library = libraries.first()
    librarians = Librarian.objects.filter(library=library)
    if librarians.exists():
        librarian = librarians.first()
        print(librarian.name)
    else:
        print("Librarian not found.")
else:
    print("Library not found.")
