from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feeds.views import FeedViewSet

router = DefaultRouter()
router.register('', FeedViewSet)

urlpatterns = [
    path('', include(router.urls))
]
