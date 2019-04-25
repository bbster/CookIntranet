from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from authen.serializers import MemberSerializers
from .models import Member


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class MemberViewSet(viewsets.ModelViewSet):
    # 회원가입을 할땐, 권한 체크 X
    serializer_class = MemberSerializers
    queryset = Member.objects.all()

    # POST  => 회원가입
    def create(self, request, *args, **kwargs):  # Y
        print("MemberViewSet 의 create 함수 실행됨")
        return super().create(request, *args, **kwargs)

    # GET : 리스트  (질문: 권한없는사람이 이거 실행해도됨?) N
    def list(self, request, *args, **kwargs):
        print("MemberViewSet 의 list 함수 실행됨")
        # 권한체크로직이 필요
        return super().list(request, *args, **kwargs)

    # GET 상세  (질문: 권한없는사람이 이거 실행해도됨?) N
    def retrieve(self, request, *args, **kwargs):
        # 권한체크로직이 필요
        return super().retrieve(request, *args, **kwargs)

    # PUT  (질문: 권한없는사람이 이거 실행해도됨?) N
    def update(self, request, *args, **kwargs):
        print("MemberViewSet 의 update 함수 실행됨")
        # 권한체크로직이 필요
        return super().update(request, *args, **kwargs)

    # DELETE  (질문: 권한없는사람이 이거 실행해도됨?) N
    def destroy(self, request, *args, **kwargs):
        print("MemberViewSet 의 Delete 함수 실행됨")
        # 권한체크로직이 필요
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def login(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        for user in User.objects.all():
            Token.objects.create(user=user)
        user = authenticate(username=username, password=password)
        if not user:
            return HttpResponse("사용자가 아닙니다")
        else:
            return HttpResponse("오오 사용자다 헐!")

    @action(detail=False, methods=['get'])
    def custom(self, request):
        return Response("")

    @action(detail=True, methods=['get', 'post'])
    def custom_detail(self, request, pk):
        if request.method == "GET":
            return Response("")
        else:  # POST
            return Response("")
