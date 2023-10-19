from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView

from django.conf import settings

from .models import User
from .token import TokenTypes, AuthTokenMixin, get_token_data
from .serializers import (RegistrationSerializer,
                          ChangeEmailSerializer,
                          SendPasswordResetMailSerializer,
                          PasswordResetSerializer,
                          UserSerializer,
                          ChangePasswordSerializer, UserCreditsSerializer)
from .permissions import IsNotAuthenticated, IsUserOrReadOnly
from .services import get_jwt_tokens_for_user, get_user_credits, get_client_ip

from apps.picsart.models import UserFunctionsUsageCounter


class UserRegistrationAPIView(AuthTokenMixin,
                              generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsNotAuthenticated]
    token_type = TokenTypes.SIGNUP
    html_message_template = 'users/confirm_email_message.html'
    mail_with_celery = False
    front_url = settings.EMAIL_CONFIRMATION_URL

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        tokenized_mail_message = self.send_tokenized_mail(
            self.request.data['email'])

        return Response({
            'status': 200,
            'message': tokenized_mail_message,
            'user': response.data
        }, status=status.HTTP_200_OK)


class ConfirmEmailAPIView(AuthTokenMixin,
                          APIView):
    permission_classes = [IsNotAuthenticated]
    token_type = TokenTypes.SIGNUP

    def post(self, *args, **kwargs):
        token = self.kwargs.pop('token')
        email = self.kwargs.pop('email')
        token_data = get_token_data(token, email)
        if token_data.token:
            user = User.objects.get(email=email)
            user.is_active = True
            user.save()
            token_data.token.delete()
            if not UserFunctionsUsageCounter.objects.filter(user=user).exists():
                UserFunctionsUsageCounter.objects.get_or_create(user=user)
            return Response(
                data=get_jwt_tokens_for_user(user),
                status=status.HTTP_200_OK
            )
        else:
            return Response({'error': token_data.error}, status=status.HTTP_400_BAD_REQUEST)


class ChangeEmailAPIView(AuthTokenMixin,
                         APIView):
    serializer_class = ChangeEmailSerializer
    permission_classes = [IsAuthenticated]
    token_type = TokenTypes.CHANGE_EMAIL
    html_message_template = 'users/confirm_email_changing.html'
    mail_with_celery = False
    front_url = settings.CHANGE_EMAIL_CONFIRMATION_URL

    def post(self, *args, **kwargs):
        serializer = ChangeEmailSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        email = self.request.data['email']
        tokenized_mail_message = self.send_tokenized_mail(email)
        return Response({
            'success': tokenized_mail_message
        }, status=status.HTTP_200_OK)


class ChangeEmailConfirmAPIView(AuthTokenMixin,
                                APIView):
    permission_classes = [IsAuthenticated]
    token_type = TokenTypes.CHANGE_EMAIL

    def post(self, *args, **kwargs):
        token = kwargs.pop('token')
        new_email = kwargs.pop('email')
        token_data = get_token_data(token, new_email)
        if token_data.token:
            user = self.request.user
            user.email = new_email
            user.save()
            token_data.token.delete()
            return Response({
                'success': 'You successfully changed your email'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': token_data.error
            }, status=status.HTTP_400_BAD_REQUEST)


class SendPasswordResetAPIView(AuthTokenMixin,
                               APIView):
    serializer_class = SendPasswordResetMailSerializer
    token_type = TokenTypes.PASSWORD_RESET
    html_message_template = 'users/password_reset_msg.html'
    mail_with_celery = False
    front_url = settings.RESET_PASSWORD_CONFIRMATION_URL

    def post(self, *args, **kwargs):
        serializer = SendPasswordResetMailSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        email = self.request.data['email']
        tokenized_mail_message = self.send_tokenized_mail(email)
        return Response({'success': tokenized_mail_message},
                        status=status.HTTP_200_OK)


class PasswordResetAPIView(AuthTokenMixin,
                           APIView):
    serializer_class = PasswordResetSerializer
    token_type = TokenTypes.PASSWORD_RESET

    def post(self, *args, **kwargs):
        token = self.kwargs.pop('token')
        email = self.kwargs.pop('email')
        token_data = get_token_data(token, email)
        if token_data.token:
            serializer = PasswordResetSerializer(data=self.request.data,
                                                 context={'email': kwargs['email']})
            serializer.is_valid(raise_exception=True)
            token_data.token.delete()
            return Response({
                'success': 'Password reset success.'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': token_data.error
            }, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordAPIView(APIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        if not self.request.user.check_password(
                serializer.data.get('old_password')
        ):
            return Response({
                'error': 'The old password is wrong! Check it and try again.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if serializer.data['old_password'] == serializer.data['new_password']:
            return Response({
                'error': 'The new password must be different from the old one!'
            }, status=status.HTTP_400_BAD_REQUEST)

        self.request.user.set_password(serializer.data['new_password'])
        self.request.user.save()

        return Response({
            'success': 'You successfully changed your password!'
        }, status=status.HTTP_200_OK)


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserOrReadOnly]

    def get_object(self):
        return User.objects.get(id=self.request.user.id)


class UserCredits(APIView):
    serializer_class = UserCreditsSerializer

    def post(self, *args, **kwargs):
        user_authenticated = self.request.user.is_authenticated
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        ip_address = serializer.data.get('ip_address')

        if user_authenticated:
            user_id = self.request.user.id
        else:
            user_id = None

        user_credits = get_user_credits(ip_address, user_authenticated, user_id)
        return Response(data=user_credits, status=status.HTTP_200_OK)


class GetClientIpAPIView(APIView):

    def get(self, *args, **kwargs):
        ip = get_client_ip(self.request)
        return Response({
            'ip': ip
        }, status=status.HTTP_200_OK)
