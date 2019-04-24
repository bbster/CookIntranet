from django.urls import include, path

from rest_framework import routers
from authen.views import *

router = routers.DefaultRouter()
router.register('members', MemberViewSet)


# base: django
# second lib: rest_framework

# 1. 회원가입
# POST www.test.com/auth/members/   => create
# GET www.test.com/auth/members/    => list
# GET www.test.com/auth/members/23/    => retrieve
# PUT www.test.com/auth/members/23/     => update
# DELETE www.test.com/auth/members/23/     => update

# {"username":~~, "password": ~~~, "phone_number": ~~}
# 1. POST 로 요청하면 "rest_framework" 는 create함수를 실행함

# REST :
# crud
# POST -> Create
# GET -> Read --> rest 에서는 list 형식과 하나를 콕찝어서 조회하는 방식(상세페이지)
# PUT -> Update
# DELETE -> DELETE


urlpatterns = [
    #path('', include('rest_auth.urls')),
    path('', include(router.urls)),
]
