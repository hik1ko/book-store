import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from config.swagger import swagger_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/v1', include('apps.account.urls')),
    path('api/book/v1/', include('apps.book.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += swagger_patterns
if os.getenv("USE_S3") != 'True':
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
