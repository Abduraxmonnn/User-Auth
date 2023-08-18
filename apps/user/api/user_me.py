# Rest-Framework
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.user.models import CustomUser
from apps.user.serializers import CustomUserListSerializer


class UserMeAPIView(APIView):
    def get(self, request, phone_number):
        try:
            get_user = CustomUser.objects.get(phone_number=phone_number)
            filter_user = CustomUser.objects.filter(another_invite_code=get_user.invite_code)

            user_list = []

            for i in filter_user:
                user_list.append(i.phone_number)

            return Response({
                "current_user": get_user.phone_number,
                "current_user_invite_code": get_user.invite_code,
                "phone_number": user_list
            }, 200)

        except CustomUser.DoesNotExist:
            return Response({
                "message": "User does not Exists"
            }, 200)
