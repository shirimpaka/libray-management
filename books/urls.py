from django.urls import path
from .views import Home

urlpatterns = [
    path('books/', Home.as_view() ),
]
