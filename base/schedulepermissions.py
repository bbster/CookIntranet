import jwt
from rest_framework.permissions import BasePermission as DRFBasePermission
from authen.models import Member
from cook_intra import settings_base


class BasePermission(DRFBasePermission):
    def has_permission(self, request, view):  # 사용자 지정 권한
        if view.action == "schedulelist":             # view.action  schedule_list
            return True  # permission True
        if view.action == "createschedule":             # view.action  schedule_list
            return True  # permission True
        if view.action == "updateschedule":             # view.action  schedule_list
            return True  # permission True
        if view.action == "deleteschedule":             # view.action  schedule_list
            return True  # permission True
        else:
            # token = request.data.get("token", None)
            # if not token:
            #     return False
            # try:
            #     user_info = jwt.decode(token, settings_base.SECRET_KEY, algorithms=['HS256'])  # jwt token decode
            #     user = Member.objects.get(user_info["username"])
            #     request.user = user
            #     return True
            # except Exception as e:
                return True

    # def has_object_permission(self, request, view, obj):
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
