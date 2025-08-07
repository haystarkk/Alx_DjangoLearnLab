from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """API endpoint that allows authors to be viewed or edited"""
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """API endpoint that allows books to be viewed or edited"""
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
