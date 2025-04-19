from .views import delete_book, edit_book, home, addBook, book
from django.urls import path

urlpatterns = [
    path('add/', addBook, name='addBook'),
    path('<int:book_id>/', book, name='book'),
    path('<int:book_id>/delete/', delete_book, name='delete_book'),
    path('<int:book_id>/edit/', edit_book, name='edit_book'),
]