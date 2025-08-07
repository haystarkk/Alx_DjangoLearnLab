from rest_framework import generics, permissions
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

class BookCreateView(CreateAPIView):
    """
    View specifically for creating books
    POST /books/create/ - Create new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Save the book with the requesting user as owner"""
        serializer.save(owner=self.request.user)

class BookUpdateView(UpdateAPIView):
    """
    View specifically for updating books
    PUT /books/<pk>/update/ - Update book
    PATCH /books/<pk>/update/ - Partial update book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(DestroyAPIView):
    """
    View specifically for deleting books
    DELETE /books/<pk>/delete/ - Delete book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookListView(ListCreateAPIView):
    """
    Combined view for listing and creating books
    GET /books/ - List all books
    POST /books/ - Create new book
    """
    queryset = Book.objects.all().order_by('-publication_year')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetailView(RetrieveUpdateDestroyAPIView):
    """
    Combined view for retrieve/update/delete
    GET /books/<pk>/ - Retrieve book
    PUT /books/<pk>/ - Update book
    DELETE /books/<pk>/ - Delete book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
