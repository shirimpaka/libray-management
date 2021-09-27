from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from .models import Book

class Home(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = 'books'
