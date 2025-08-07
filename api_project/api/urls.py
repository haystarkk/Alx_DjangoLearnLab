from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    # Original list view (kept for backward compatibility)
    path('books-list/', BookList.as_view(), name='book-list'),
    
    # Include all ViewSet URLs
    path('', include(router.urls)),
]
