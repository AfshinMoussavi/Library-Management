from .views import book_list
from django.urls import path

app_name = 'book'

urlpatterns = [
    path('', book_list, name='book_list'),
]