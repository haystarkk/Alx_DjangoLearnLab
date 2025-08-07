from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    """Represents an author who writes books"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    """Represents a book written by an author"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    class Meta:
        unique_together = ['title', 'author']
