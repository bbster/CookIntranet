from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from .serializers import *
from .models import Member


# 멤버뷰셋 멤버오브젝트 반환? 이것도 잘모르겠음
class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MemberSerializers
    queryset = Member.objects.all()

    # POST
    def create(self, request, *args, **kwargs):
        pass

    # GET : 리스트
    def list(self, request, *args, **kwargs):
        pass

    # GET 상세
    def retrieve(self, request, *args, **kwargs):
        pass

    # PUT
    def update(self, request, *args, **kwargs):
        pass

    # DELETE
    def destroy(self, request, *args, **kwargs):
        pass


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