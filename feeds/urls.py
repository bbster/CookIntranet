from django.urls import path

from feeds.views import broadcast, conversations, delivered, delete

urlpatterns = [
    path('conversation/', broadcast),
    path('conversations/', conversations),
    path('conversations/<int:id>/delivered/', delivered),
    path('conversations/<int:id>/delete/', delete),
    ]

