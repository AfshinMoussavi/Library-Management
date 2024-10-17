from . import views
from django.urls import path

app_name = 'book'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/book/', views.book_create, name='book_create'),
    path('update/book/<int:pk>/', views.book_update, name='book_update'),
    path('delete/book/<int:pk>/', views.book_delete, name='book_delete'),
    path('borrowed_books/', views.borrowed_books, name='borrowed_books'),
    path('borrow_book/<int:pk>/', views.borrow_book, name='borrow_book'),
    path('retake_book/<int:pk>/', views.retake_book, name='retake_book'),
    
]