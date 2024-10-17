from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, BorrowedBook
from .forms import BookForm, BorrowBookForm

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'BooksManagement/book_list.html', context)

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book:book_list')
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'BooksManagement/book_create.html', context)

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book:book_list')
    else:
        form = BookForm(instance=book)
    context = {'form': form}
    return render(request, 'BooksManagement/book_update.html', context)

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book:book_list')
    context = {'book': book}
    return render(request, 'BooksManagement/book_delete.html', context)

def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.all()
    
    context = {'borrowed_books': borrowed_books}
    return render(request, 'BooksManagement/borrowed_books.html', context)

def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk, is_available=True)
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            borrowed_book = form.save(commit=False)
            borrowed_book.book = book
            borrowed_book.save()
            book.is_available = False
            book.save()
            return redirect('book:borrowed_books')
    else:
        form = BorrowBookForm()
    
    context = {'form':form, 'book':book}
    return render(request, 'BooksManagement/borrow_book.html', context)


def retake_book(request, pk):
    book = get_object_or_404(Book, pk=pk, is_available=False)
    borrowed_book = get_object_or_404(BorrowedBook, book=book)
    if request.method == 'POST':
        book.is_available = True
        book.save()
        borrowed_book.delete()
        return redirect('book:borrowed_books')
    context = {'book':book}
    return render(request, 'BooksManagement/retake_book.html', context)