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
from django.contrib import admin
from django.urls import include, path
from cook_intra import views


urlpatterns = [
    path('admin/', admin.site.urls),  # 장고어드민
    #path('api/v1/authen/', include('authen.urls')),
    path('auth/', include('authen.urls')),  # 회원관련
    path('api/v1/feeds/', include('feeds.urls')),
]

urlpatterns += [
    path('', views.VueAppView.as_view()),
]