from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Filtering, Searching & Ordering configuration
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Filtering fields
    filterset_fields = {
        'title': ['exact', 'icontains'],
        'author': ['exact', 'icontains'],
        'publication_year': ['exact', 'gte', 'lte'],
        'genre': ['exact'],
    }
    
    # Search fields
    search_fields = ['title', 'author', 'description']
    
    # Ordering fields
    ordering_fields = ['title', 'author', 'publication_year', 'created_at']
    ordering = ['title']  # Default ordering

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
