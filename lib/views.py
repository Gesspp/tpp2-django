from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import AddBookForm
from django.contrib.auth.decorators import login_required
from .models import Book

def home(request):
    return render(request, 'index.html', {'books': Book.objects.all()})

@login_required
def addBook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('home')
    else:
        form = AddBookForm()
    return render(request, 'addBook.html', {'form': form})

@login_required
def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book.html', {'book': book})

@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddBookForm(instance=book)
    return render(request, 'edit.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('home')