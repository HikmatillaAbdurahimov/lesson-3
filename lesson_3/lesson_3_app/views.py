from django.shortcuts import render
from .models import Books

def home(request):
    return render(request, 'home.html')

def books(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})

def authors(request):
    pass
