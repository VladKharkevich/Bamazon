from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class Author(AbstractUser):
	# Author of books
	books = models.ManyToManyField('Book', blank=True)

	def get_absolute_url(self):
		return reverse('author_detail_url', kwargs={'pk': self.pk})


class Book(models.Model):
	# Book for selling 
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, unique=True)
	description = models.TextField(null=True, blank=True)
	authors = models.ManyToManyField(Author, through=Author.books.through)

	def get_absolute_url(self):
		return reverse('book_detail_url', kwargs={'slug': self.slug})

	def __str__(self):
		return self.title