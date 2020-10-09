from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from .models import Author, Book


class MainPage(View):
	''' Start page '''
	def get(self, request):
		return render(request, "BamazonApp/index.html")


class BookList(ListView):
	''' List of books '''
	template_name = "BamazonApp/books_list.html"
	model = Book
	paginate_by = 2



class BookDetail(DetailView):
	''' Information about book '''
	template_name = "BamazonApp/book_detail.html"
	model = Book


class AuthorList(ListView):
	''' List of authors '''
	template_name = "BamazonApp/authors_list.html"
	model = Author
	paginate_by = 2


class AuthorDetail(DetailView):
	''' Information about author '''
	template_name = "BamazonApp/author_detail.html"
	model = Author	
