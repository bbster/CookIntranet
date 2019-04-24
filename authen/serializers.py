from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Member


class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("id", "first_name", "last_name", "phone_number")


# 회원 가입 // 뭔지 정확히 다 파악못함
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone_number")

        def create(self, validated_data):
            user = User.objects.create_user(
                validated_data["username"], None, validated_data["password"]
            )
            return user


# 접속 유지중인지 확인  ID와 성씨
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name")


# 로그인
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("로그인 안됨 확인 요망")
