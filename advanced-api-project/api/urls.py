from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookListCreateView,
    BookRetrieveUpdateDestroyView
)

urlpatterns = [
    # Separate endpoints style
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),

    # RESTful combined endpoints style
    path('books/combined/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/combined/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), 
         name='book-retrieve-update-destroy'),
]
