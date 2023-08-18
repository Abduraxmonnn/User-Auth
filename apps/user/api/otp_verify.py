# Django
from django.shortcuts import get_object_or_404

# Rest-Framework
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.user.models import CustomUser
from apps.user.serializers import OTPVerifySerializer


class OTPVerifyAPIView(APIView):
    def post(self, request, phone_number):
        serializer = OTPVerifySerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data['otp_code']

        get_user = CustomUser.objects.filter(phone_number=phone_number, otp=otp_code).first()

        if get_user:
            get_user.is_active = True
            get_user.save()
            return Response({
                'message': 'User account have been activated'
            }, 200)
        else:
            return Response({
                'message': 'OTP code incorrect. Please try again'
            }, 400)
