# Rest-Framework
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.user.models import CustomUser
from apps.user.serializers import CustomUserListSerializer


class GetOTPAPIView(APIView):
    def get(self, request, phone_number):
        try:
            get_user = CustomUser.objects.get(phone_number=phone_number)

            return Response({
                "otp_code": get_user.otp
            }, 200)

        except CustomUser.DoesNotExist:
            return Response({
                "message": "User does not Exists"
            }, 200)
