import jwt
from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from authen.serializers import MemberSerializers
from base.permissions import BasePermission
from cook_intra import settings_base
from .models import Member


class MemberViewSet(viewsets.ModelViewSet):
    # 회원가입을 할땐, 권한 체크 X
    serializer_class = MemberSerializers
    queryset = Member.objects.all()
    permission_classes = (BasePermission, )

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
            return Response({'Error': "ERROR"}, status=400)

    @action(detail=False, methods=['POST'])  # token header value decode
    def decode_jwt_token(self, request, *args, **kwargs):
        token = request.data.get('token')  # Json 데이터형식 헤더값 받아옴
        payload = jwt.decode(token, settings_base.SECRET_KEY, algorithms=['HS256'])  # jwt token decode
        username = payload['username']  # decode 값 담기
        return Response({"반환완료": username}, status=200)

    @action(detail=False, methods=['get'])
    def test(self, request, *args, **kwargs):
        return Response({"msg": "OK"}, status=200)

    #
    # # GET : 리스트  (질문: 권한없는사람이 이거 실행해도됨?) N
    # def list(self, request, *args, **kwargs):
    #     print("MemberViewSet 의 list 함수 실행됨")
    #     # 권한체크로직이 필요
    #     return super().list(request, *args, **kwargs)
    #
    # # GET 상세  (질문: 권한없는사람이 이거 실행해도됨?) N
    # def retrieve(self, request, *args, **kwargs):
    #     # 권한체크로직이 필요
    #     return super().retrieve(request, *args, **kwargs)
    #
    # # PUT  (질문: 권한없는사람이 이거 실행해도됨?) N
    # def update(self, request, *args, **kwargs):
    #     print("MemberViewSet 의 update 함수 실행됨")
    #     # 권한체크로직이 필요
    #     return super().update(request, *args, **kwargs)
    #
    # # DELETE  (질문: 권한없는사람이 이거 실행해도됨?) N
    # def destroy(self, request, *args, **kwargs):
    #     print("MemberViewSet 의 Delete 함수 실행됨")
    #     # 권한체크로직이 필요
    #     return super().destroy(request, *args, **kwargs)
    # @action(detail=False, methods=['get'])
    # def custom(self, request):
    #     return Response("")
    #
    # @action(detail=True, methods=['get', 'post'])
    # def custom_detail(self, request, pk):
    #     if request.method == "GET":
    #         return Response("")
    #     else:  # POST
    #         return Response("")
