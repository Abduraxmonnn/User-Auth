# Rest-Framework
from rest_framework.response import Response
from rest_framework.views import APIView

# Project
from apps.user.models import CustomUser
from apps.user.serializers import ActivateInviteCodeSerializer


class ActivateInviteCodeAPIView(APIView):
    def post(self, request, phone_number):
        serializer = ActivateInviteCodeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        invite_code = serializer.validated_data['invite_code']

        check_exists_code = CustomUser.objects.filter(invite_code=invite_code)

        if check_exists_code.exists():
            get_current_user = CustomUser.objects.get(phone_number=phone_number)
            if get_current_user.is_active is True:
                if get_current_user.another_invite_code is None:
                    get_current_user.another_invite_code = invite_code
                    get_current_user.save()

                    return Response({
                        'message': 'Invite Code has been Activated'
                    }, 200)

                return Response({
                    'message': 'User has already used an invitation code'
                }, 400)

            return Response({
                'message': 'User must be activated'
            }, 400)

        return Response({
            'message': 'invitation code does not Exists'
        }, 400)
