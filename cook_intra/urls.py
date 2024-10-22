from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from cook_intra import views, settings_base
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),  # 장고어드민
    path('api/', include('authen.urls')),  # 회원관련
    path('api/feeds/', include('feeds.urls')),  # 게시판
    path('api/scheduler/', include('scheduler.urls')),  # 스케줄
    path('api/token/', obtain_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/token/verify/', verify_jwt_token),
]

urlpatterns += [
    path('', views.VueAppView.as_view()),
]

urlpatterns += static(settings_base.MEDIA_URL, document_root=settings_base.MEDIA_ROOT)
