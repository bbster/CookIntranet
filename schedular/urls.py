from django.urls import path, include
from rest_framework.routers import DefaultRouter

from schedular.views import ScheduleViewSet

router = DefaultRouter()
router.register('', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls))
]
