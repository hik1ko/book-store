from django.urls import path

from apps.account.api_endpoints.auth.Login import LoginView
from apps.account.api_endpoints.auth.Register import RegisterView
from apps.account.api_endpoints.passwordreset import RequestPasswordReset, ResetPasswordAPIView

app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('reset-password-request/', RequestPasswordReset.as_view(), name='request_password_reset'),
    path('reset-password/<str:token>/', ResetPasswordAPIView.as_view(), name='reset-password'),
]
