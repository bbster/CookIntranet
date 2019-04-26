"""cook_intra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# demo_project/urls.py
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from cook_intra import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),  # 장고어드민
    path('auth/', include('authen.urls')),  # 회원관련
    path('feeds/', include('feeds.urls')),
    path('api/token/', obtain_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify/', verify_jwt_token),

]

urlpatterns += [
    path('', views.VueAppView.as_view()),
]