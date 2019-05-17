from django.urls import path

from pushers.views import broadcast, conversations, delivered

urlpatterns = [
    path('conversation/', broadcast),
    path('conversations/', conversations),
    path('conversations/<int:id>/delivered/', delivered),
    ]

