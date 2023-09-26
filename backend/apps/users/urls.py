from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

from .views import (UserRegistrationAPIView,
                    ConfirmEmailAPIView,
                    ChangeEmailAPIView,
                    ChangeEmailConfirmAPIView,
                    SendPasswordResetAPIView,
                    PasswordResetAPIView,
                    UserAPIView)

urlpatterns = [
    path('registration/', UserRegistrationAPIView.as_view(), name='registration'),
    path('confirm_email/<token>/<email>/', ConfirmEmailAPIView.as_view(), name='confirm-email'),
    path('change_email/', ChangeEmailAPIView.as_view(), name='change_email_send'),
    path('change_email_confirm/<token>/<email>/',
         ChangeEmailConfirmAPIView.as_view(),
         name='change_email_confirm'),
    path('password_reset/', SendPasswordResetAPIView.as_view(), name='send_password_reset'),
    path('password_reset/<token>/<email>/', PasswordResetAPIView.as_view(), name='password_reset'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('user/', UserAPIView.as_view(), name='user')
]
