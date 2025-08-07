from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author', 'owner']
        extra_kwargs = {
            'author': {'required': True}
        }

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Max allowed: {current_year}"
            )
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
