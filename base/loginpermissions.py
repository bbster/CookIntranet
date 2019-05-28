import jwt
from rest_framework.permissions import BasePermission as DRFBasePermission
from authen.models import Member
from cook_intra import settings_base


class BasePermission(DRFBasePermission):
    def has_permission(self, request, view):  # 사용자 지정 권한
        if view.action == "login":  # view.decode_jwt_token 조인
            return True
        elif view.action == "verify":  # view.decode_jwt_token 조인
            return True
        else:
            token = request.data.get("token", None)
            if not token:
                return False
            try:
                user_info = jwt.decode(token, settings_base.SECRET_KEY, algorithms=['HS256'])  # jwt token decode
                user = Member.objects.get(user_info["username"])
                request.user = user
                return True
            except Exception as e:
                return False

    def has_object_permission(self, request, view, obj):
        token = request.data.get("token", None)
        if not token:
            return False
        try:
            user_info = jwt.decode(token, settings_base.SECRET_KEY, algorithms=['HS256'])  # jwt token decode
            user = Member.objects.get(user_info["username"])
            request.user = user
            return True
        except Exception as e:
            return False
