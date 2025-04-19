from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    public_date = models.DateField()
    image = models.ImageField(upload_to='books/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
