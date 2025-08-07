from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows books to be viewed or created.
    
    Filtering:
    - title: exact match or contains (icontains)
    - author: exact match or contains (icontains)
    - publication_year: exact, gte (greater than or equal), lte (less than or equal)
    - genre: exact match
    
    Searching:
    - Searches across title, author, and description fields
    
    Ordering:
    - title, author, publication_year, created_at
    - Add '-' prefix for descending order
    - Default ordering: title (ascending)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # All filter backends now come from django_filters
    filter_backends = [
        filters.DjangoFilterBackend,
        filters.SearchFilter,  # Using django_filters' SearchFilter
        filters.OrderingFilter
    ]
    
    filterset_fields = {
        'title': ['exact', 'icontains'],
        'author': ['exact', 'icontains'],
        'publication_year': ['exact', 'gte', 'lte'],
        'genre': ['exact'],
    }
    
    search_fields = ['title', 'author', 'description']
    ordering_fields = ['title', 'author', 'publication_year', 'created_at']
    ordering = ['title']  # Default ordering

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
