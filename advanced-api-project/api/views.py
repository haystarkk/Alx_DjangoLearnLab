from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    """
    View to list all books or create a new book
    GET /books/ - List all books
    POST /books/ - Create new book (authenticated only)
    """
    queryset = Book.objects.all().order_by('-publication_year')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Save the book with the requesting user as owner"""
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a book
    GET /books/<pk>/ - Retrieve book
    PUT /books/<pk>/ - Update book (owner or admin only)
    DELETE /books/<pk>/ - Delete book (owner or admin only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorListView(generics.ListAPIView):
    """
    View to list all authors
    GET /authors/ - List all authors
    """
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    """
    View to retrieve an author
    GET /authors/<pk>/ - Retrieve author details
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
