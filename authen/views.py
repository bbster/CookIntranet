import jwt
from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from authen.serializers import MemberSerializers, LoginSerializers, VerifySerializers
from base import basepermissions, loginpermissions
from cook_intra import settings_base
from .models import Member
from django.http import HttpResponseBadRequest


class MemberViewSet(viewsets.ModelViewSet):
    # 회원가입을 할땐, 권한 체크 X
    serializer_class = MemberSerializers
    queryset = Member.objects.all()
    permission_classes = (basepermissions.BasePermission,)

    # POST : 생성
    @action(detail=False, methods=['POST'])
    def join(self, request, *args, **kwargs):
        # 회원가입
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        if not username:
            return Response({"msg": "'username' 파라미터는 필수값입니다."})
        if not password:
            return Response({"msg": "'password' 파라미터는 필수값입니다."})
        try:
            saved_user = Member.objects.create_user(**request.data)
        except:
            return Response({"msg": "요청 파라미터가 잘못되었습니다."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(saved_user)
        data = serializer.data
        data.update({"msg": "회원가입에 성공하였습니다."})
        return Response(data, status=status.HTTP_201_CREATED)


class LoginViewSet(viewsets.ModelViewSet):

    serializer_class = LoginSerializers
    queryset = Member.objects.all()
    permission_classes = (loginpermissions.BasePermission,)

    @action(detail=False, methods=['POST'])
    def login(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        user = authenticate(username=username, password=password)
        # LOGIN 할때 JWT TOKEN 발급
        if user is not None:
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            # JWT TOKEN RESPONSE
            return Response({"token": token}, status=200)
        else:
            return Response({"Error": "ERROR"}, status=400)


class VerifyViewSet(viewsets.ModelViewSet):
    serializer_class = VerifySerializers
    queryset = Member.objects.all()
    permission_classes = (loginpermissions.BasePermission,)
    @action(detail=False, methods=['POST'])  # token header value decode
    def verify(self, request, *args, **kwargs):
        token = request.data.get('token')  # Json 데이터형식 헤더값 받아옴
        try:
            payload = jwt.decode(token, settings_base.SECRET_KEY, algorithms=['HS256'])  # jwt token decode
        except jwt.DecodeError:
            raise HttpResponseBadRequest
        user = payload['username']  # decode 값 담기
        id = payload['user_id']
        #index 값 같이 반환 추가해야
        return Response({"token": token, "username": user, "id": id}, status=200)
