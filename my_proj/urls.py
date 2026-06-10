
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('account.api.urls')),
    path('api/gym/', include('gym.api.urls')),
    path('books/', include("books.urls")),

]
