from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import AuthorSerializer, BookSerializer
from BamazonApp.models import Author, Book


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
