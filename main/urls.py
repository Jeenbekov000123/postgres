from django.urls import path
from .views import index, home

urlpatterns = [
    path("area", home),
    path("index/", index),
    path("home/", home),
]
