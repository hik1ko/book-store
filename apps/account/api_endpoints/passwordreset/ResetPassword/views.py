from rest_framework import generics, permissions
from rest_framework.response import Response

from apps.account.api_endpoints.passwordreset.ResetPassword.serializers import ResetPasswordSerializer
from apps.account.models import PasswordReset, User


class ResetPasswordAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        reset_obj = PasswordReset.objects.filter(token=token).first()

        if not reset_obj:
            return Response({'error': 'Invalid token'}, status=400)

        user = User.objects.filter(email=reset_obj.email).first()

        if user:
            user.set_password(request.data['new_password'])
            user.save()

            reset_obj.delete()

            return Response({'success': 'Password updated'})
        else:
            return Response({'error': 'No user found'}, status=404)