from django.urls import path
from rest_framework.routers import DefaultRouter
from books.views import CategoryApi, BooksApi

router = DefaultRouter()
router.register("category", CategoryApi, basename="category")
router.register("book", BooksApi, basename="books")
urlpatterns = [

]+router.urls