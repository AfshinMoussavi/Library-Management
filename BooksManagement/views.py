from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


def book_list(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'BooksManagement/book_list.html', context)
