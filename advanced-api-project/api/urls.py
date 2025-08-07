from django.urls import path
from .views import (
    book_list,
    book_detail,
    book_update,
    book_delete
)

urlpatterns = [
    # Basic CRUD endpoints
    path('books/', book_list, name='book-list'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    
    # Explicit update/delete endpoints
    path('books/update/<int:pk>/', book_update, name='book-update'),
    path('books/delete/<int:pk>/', book_delete, name='book-delete'),
    
    # Alternative RESTful structure (optional)
    path('books/<int:pk>/update/', book_update, name='book-update-alt'),
    path('books/<int:pk>/delete/', book_delete, name='book-delete-alt'),
]
