from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'public_date', 'description', 'image']
        widgets = {
            'public_date': forms.DateInput(attrs={'type': 'date'})
        }