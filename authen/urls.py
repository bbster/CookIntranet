from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('rest_auth.urls')),
]