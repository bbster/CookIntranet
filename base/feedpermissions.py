import jwt
from authen.models import Member
from cook_intra import settings_base
from rest_framework.permissions import BasePermission as DRFBasePermission


class BasePermission(DRFBasePermission):
    def has_permission(self, request, view):  # 사용자 지정 권한
        if view.action == "conversations":    # view.action  feed list
            return True  # permission True
        # elif view.action == "conversation":  # view.decode_jwt_token 조인
        #     token = request.data.get("token", None)
        #     if not token:
        #         return False
        #     try:
        #         user_info = jwt.decode(token, settings_base.SECRET_KEY, algorithms=['HS256'])  # jwt token decode
        #         user = Member.objects.get(user_info["username"])
        #         request.user = user
        #         return True
        #     except Exception as e:
        #         return False
        #     return True
        #
        # elif view.action == "delivered":  # view.decode_jwt_token 조인
        #     token = request.data.get("token", None)
        #     if not token:
        #         return False
        #     try:
        #         user_info = jwt.decode(token, settings_base.SECRET_KEY, algorithms=['HS256'])  # jwt token decode
        #         user = Member.objects.get(user_info["username"])
        #         request.user = user
        #         return True
        #     except Exception as e:
        #         return False
        #     return True
        #
        # elif view.action == "delete":  # view.decode_jwt_token 조인
        #     token = request.data.get("token", None)
        #     if not token:
        #         return False
        #     try:
        #         user_info = jwt.decode(token, settings_base.SECRET_KEY, algorithms=['HS256'])  # jwt token decode
        #         user = Member.objects.get(user_info["username"])
        #         request.user = user
        #         return True
        #     except Exception as e:
        #         return False
        #     return True

    def has_object_permission(self, request, view, obj):
        # token = request.data.get("token", None)
        # if not token:
            return True
        # try:
        #     user_info = jwt.decode(token, settings_base.SECRET_KEY, algorithms=['HS256'])  # jwt token decode
        #     user = Member.objects.get(user_info["username"])
        #     request.user = user
        #     return True
        # except Exception as e:
        #     return False
