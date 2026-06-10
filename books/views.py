from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Book
from .serializer import CategorySerializer,BookSerializer

class CategoryApi(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BooksApi(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer