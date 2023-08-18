# Django
from django.urls import path

# Project
from apps.user.api import CustomUserAuthAPIView, OTPVerifyAPIView, ActivateInviteCodeAPIView, UserMeAPIView

urlpatterns = [
    path('auth/', CustomUserAuthAPIView.as_view(), name='user_auth'),
    path('verify/<str:phone_number>/', OTPVerifyAPIView.as_view(), name='verify_code'),
    path('activate_invite_code/<str:phone_number>/', ActivateInviteCodeAPIView.as_view(),
         name='activate_another_invite_code'),
    path('user_list/<str:phone_number>/', UserMeAPIView.as_view(), name='user_list'),
]
