from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.book.views import BookViewSet, BookCategoryViewSet, BookGenreViewSet

router = DefaultRouter()
router.register('category', BookCategoryViewSet)
router.register('book', BookViewSet)
router.register('genre', BookGenreViewSet)

urlpatterns = [
    path('', include(router.urls))
]
