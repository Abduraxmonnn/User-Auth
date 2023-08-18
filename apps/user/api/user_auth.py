# Django
from django.shortcuts import get_object_or_404

# Rest-Framework
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.user.models import CustomUser
from apps.user.serializers import CustomUserAuthSerializer, OTPVerifySerializer
from apps.services import generate_code


class CustomUserAuthAPIView(APIView):
    model = CustomUser
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserAuthSerializer

    def post(self, request):
        serializer = CustomUserAuthSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']

        check_user = CustomUser.objects.filter(phone_number=phone_number)
        if not check_user.exists():
            invite_code = generate_code(6)
            otp_code = generate_code(4)
            created = CustomUser.objects.create(phone_number=phone_number, is_active=False)
            created.invite_code = invite_code
            created.otp = otp_code
            created.save()
            return Response({
                'message': 'Phone number authorization successful. You can now proceed with the next steps.'
            }, 201)
        else:
            return Response({
                'message': 'User with this phone number already exists'
            }, 400)


class CustomUserOTPVerifyAPIView(APIView):
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        otp_code = serializer.validated_data['otp_code']

        get_user = get_object_or_404(CustomUser, otp=otp_code)

        if otp_code is get_user.otp:
            get_user.is_active = True
            return Response({
                'message': 'User account have been activated'
            }, 200)
        else:
            return Response({
                'message': 'OTP code incorrect'
            }, 400)
