# Rest-Framework
from rest_framework import serializers

# Project
from apps.user.models import CustomUser


class CustomUserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'phone_number'
        ]


class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'phone_number',
            'otp',
            'invite_code',
            'another_invite_code'
        ]


class OTPVerifySerializer(serializers.Serializer):
    otp_code = serializers.CharField(max_length=4)


class ActivateInviteCodeSerializer(serializers.Serializer):
    invite_code = serializers.CharField(max_length=6)
