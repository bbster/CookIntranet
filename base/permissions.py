from rest_framework.permissions import BasePermission as DRFBasePermission
from rest_framework_jwt.authentication import jwt_decode_handler
from authen.models import Member


class BasePermission(DRFBasePermission):
    def has_permission(self, request, view):  #  사용자 지정 권한
        if view.action == "join":             #  view.action  조인
            return True  # permission True
        elif view.action == "login":
            return True
        else:
            user_token = request.META.get("HTTP_USER_TOKEN", None)
            if not user_token:
                return False
            try:
                user_info = jwt_decode_handler(user_token)
                user = Member.objects.get(id=user_info["user_id"])
                request.user = user
                return True
            except Exception as e:
                return False

    def has_object_permission(self, request, view, obj):
        user_token = request.META.get("HTTP_USER_TOKEN", None)
        if not user_token:
            return False
        try:
            user_info = jwt_decode_handler(user_token)
            user = Member.objects.get(id=user_info["id"])
            request.user = user
            return True
        except Exception as e:
            return False
