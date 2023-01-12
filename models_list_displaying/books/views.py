from django.shortcuts import render, redirect
from django.urls import reverse
# from django.core.paginator import Paginator

from .models import Book


def books_view(request):
    return redirect(reverse('books_list'))

def books_list(request):
    template = 'books/books_list.html'
    books = Book.objects.order_by('pub_date')
    context = {'books': books}
    return render(request, template, context)

def book_in_date(request, pub_date):
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=pub_date)
    next_page = Book.objects.filter(pub_date__gt=pub_date).values_list('pub_date').order_by('pub_date')
    previous_page = Book.objects.filter(pub_date__lt=pub_date).values_list('pub_date').order_by('-pub_date')
    context = {'books': books,
               'next_page': next_page,
               'previous_page': previous_page}
    return render(request, template, context)

# Вариант 2. Работает, только если в БД у книг разные даты.
# books = Book.objects.order_by('pub_date')
    # page = [book.pub_date.strftime("%Y-%m-%d") for book in books]
    # paginator = Paginator(books, 1)
    # page_index = page.index(pub_date)
    # page_obj = paginator.get_page(page_index+1)
    # next_page = ''.join([book.pub_date.strftime("%Y-%m-%d") for count, book in enumerate(books) if count == page_index+1])
    # previous_page = ''.join([book.pub_date.strftime("%Y-%m-%d") for count, book in enumerate(books) if count == page_index -1])
    # context = {'books': page_obj,
    #            'next_page': next_page,
    #            'previous_page': previous_page}