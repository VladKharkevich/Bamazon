from django.urls import path

from .views import *


urlpatterns = [
	path('', MainPage.as_view(), name='main_page_url'),
	path('books/', BookList.as_view(), name='books_list_url'),
	path('books/<str:slug>/', BookDetail.as_view(), name='book_detail_url'),
	path('authors/', AuthorList.as_view(), name='authors_list_url'),
	path('authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail_url')
]