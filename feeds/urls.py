from django.urls import path

from feeds.views import broadcast, conversations, delivered, delete, update

urlpatterns = [
    path('conversation/', broadcast),
    path('conversations/', conversations),
    path('conversations/<int:id>/delivered/', delivered),
    path('conversations/<int:id>/update/', update),
    path('conversations/<int:id>/delete/', delete),
    # path('conversations/daterange/', daterange),
]
