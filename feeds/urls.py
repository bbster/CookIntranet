from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListFeed.as_view()),
    path('<int:pk>/', views.DetailFeed.as_view()),
]
