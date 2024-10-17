from django import forms
from .models import Book, BorrowedBook
from django.forms.widgets import DateInput



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author', 'category']
        

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['user', 'borrow_date', 'return_date']
        widgets = {
            'borrow_date': DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}),
            'return_date': DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}),
        }