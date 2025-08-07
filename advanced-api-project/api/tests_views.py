from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.admin = User.objects.create_superuser(
            username='admin',
            password='adminpass123'
        )
        
        # Create test data
        self.book1 = Book.objects.create(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
            publication_year=1925,
            genre='Classic'
        )
        self.book2 = Book.objects.create(
            title='Dune',
            author='Frank Herbert',
            publication_year=1965,
            genre='Science Fiction'
        )
        
        # API client
        self.client = APIClient()

    # Helper methods
    def authenticate_user(self, user=None):
        if not user:
            user = self.user
        self.client.force_authenticate(user=user)

    # CRUD Tests
    def test_list_books_unauthenticated(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        self.authenticate_user()
        url = reverse('book-list')
        data = {
            'title': 'New Book',
            'author': 'Test Author',
            'publication_year': 2023,
            'genre': 'Fiction'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        url = reverse('book-list')
        data = {'title': 'Should Fail'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_book_detail(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'The Great Gatsby')

    def test_update_book(self):
        self.authenticate_user()
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Updated Title'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book(self):
        self.authenticate_user(self.admin)  # Only admin can delete
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Filtering, Searching, Ordering Tests
    def test_filter_by_genre(self):
        url = reverse('book-list')
        response = self.client.get(url, {'genre': 'Science Fiction'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Dune')

    def test_search_by_author(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Fitzgerald'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Great Gatsby')

    def test_ordering_by_year(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Dune')
        self.assertEqual(response.data[1]['title'], 'The Great Gatsby')

    def test_combined_filters(self):
        url = reverse('book-list')
        response = self.client.get(url, {
            'search': 'great',
            'ordering': 'title'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Great Gatsby')

    # Permission Tests
    def test_unauthenticated_update(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.patch(url, {'title': 'Should Fail'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_admin_delete(self):
        self.authenticate_user()  # Regular user, not admin
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
