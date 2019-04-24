from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from .models import Member


# 멤버뷰셋 멤버오브젝트 반환? 이것도 잘모르겠음
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
        # 권한체크로직이 필요
        return super().update(request, *args, **kwargs)

    # DELETE  (질문: 권한없는사람이 이거 실행해도됨?) N
    def destroy(self, request, *args, **kwargs):
        # 권한체크로직이 필요
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def custom(self, request):
        return Response("")

    @action(detail=True, methods=['get', 'post'])
    def custom_detail(self, request, pk):
        if request.method == "GET":
            return Response("")
        else:  # POST
            return Response("")


# 사용자추가? 토큰 생성도 함 뭘까?
class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["username"])<6 or len(request.data["password"])<4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": Token.objects.create(user),
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()).data,
                "token": Token.objects.create(user),
            }
        )


# 뭔지 모름 ㅇㅇ;;
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = User

    def get_object(self):
        return self.request.user

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)