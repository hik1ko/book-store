from rest_framework import generics, permissions

from apps.account.api_endpoints.auth.Register.serializers import RegisterSerializer
from apps.account.models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

__all__ = ("RegisterView",)
