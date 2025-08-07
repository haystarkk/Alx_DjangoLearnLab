from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on Books.
    Provides the following actions:
    - list: GET /books_all/
    - create: POST /books_all/
    - retrieve: GET /books_all/<pk>/
    - update: PUT /books_all/<pk>/
    - partial_update: PATCH /books_all/<pk>/
    - destroy: DELETE /books_all/<pk>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Keep the existing BookList view if needed for backward compatibility
from rest_framework import generics
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
