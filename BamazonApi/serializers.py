from rest_framework import serializers
from BamazonApp.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		exclude = ['authors']


class AuthorSerializer(serializers.ModelSerializer):
	books = BookSerializer(many=True, read_only=True)

	class Meta:
		model = Author
		fields = ['id', 'username', 'books']