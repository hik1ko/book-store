from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from apps.account.api_endpoints.passwordreset.ResetRequest.serializers import ResetPasswordRequestSerializer
from apps.account.models import PasswordReset, User
import os

from apps.account.tasks import send_email


class RequestPasswordReset(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        email = request.data['email']
        user = User.objects.filter(email__iexact=email).first()

        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            reset = PasswordReset(email=email, token=token)
            reset.save()

            reset_url = f"{os.environ['PASSWORD_RESET_BASE_URL']}/{token}"
            subject = "Password Reset"
            message = f"Your Reset link {reset_url}"
            recipient_list = [email]
            send_email.delay(subject, message, recipient_list)

            return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User with credentials not found"}, status=status.HTTP_404_NOT_FOUND)