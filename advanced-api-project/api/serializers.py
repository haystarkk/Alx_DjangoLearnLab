from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """Serializes Book data with validation for publication year."""
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Ensure publication year is not in the future."""
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """Serializes Author data with nested BookSerializer for related books."""
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Includes nested books
