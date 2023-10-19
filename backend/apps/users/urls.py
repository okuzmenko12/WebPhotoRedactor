from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
    TokenVerifyView
)

from .views import (UserRegistrationAPIView,
                    ConfirmEmailAPIView,
                    ChangeEmailAPIView,
                    ChangeEmailConfirmAPIView,
                    SendPasswordResetAPIView,
                    PasswordResetAPIView,
                    UserAPIView,
                    ChangePasswordAPIView,
                    UserCredits,
                    GetClientIpAPIView,
                    NotAuthenticatedUserTokenAPIView)

urlpatterns = [
    path('registration/', UserRegistrationAPIView.as_view(), name='registration'),
    path('confirm_email/<str:token>/<str:email>/', ConfirmEmailAPIView.as_view(), name='confirm-email'),
    path('change_email/', ChangeEmailAPIView.as_view(), name='change_email_send'),
    path('change_email_confirm/<str:token>/<str:email>/',
         ChangeEmailConfirmAPIView.as_view(),
         name='change_email_confirm'),
    path('password_reset/', SendPasswordResetAPIView.as_view(), name='send_password_reset'),
    path('password_reset/<str:token>/<str:email>/', PasswordResetAPIView.as_view(), name='password_reset'),
    path('change_password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('user/', UserAPIView.as_view(), name='user'),
    path('user/credits/', UserCredits.as_view(), name='user_credits'),
    path('client_ip/', GetClientIpAPIView.as_view()),
    path('client_token_create/', NotAuthenticatedUserTokenAPIView.as_view())
]
