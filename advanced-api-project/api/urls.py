from django.urls import path
from . import views
from rest_framework.permissions import IsAuthenticated

urlpatterns = [
    # Book endpoints
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), 
        name='book-update'),  # Explicit update endpoint
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), 
        name='book-delete'),  # Explicit delete endpoint
    path('books/update/', views.update_book, name='update-book'),
    path('books/delete/', views.delete_book, name='delete-book'),
    
    # Author endpoints
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]
