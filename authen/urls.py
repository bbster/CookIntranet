from django.urls import include, path

from rest_framework import routers
from authen.views import *

router = routers.DefaultRouter()
router.register('register', MemberViewSet , base_name='register')

urlpatterns = [
    #path('', include('rest_auth.urls')),
    path('', include(router.urls)),

]
