from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.book.models import BookCategory, Book, BookGenre
from apps.book.serializers import BookCategorySerializer, BookSerializer, BookGenreSerializer


class BookCategoryViewSet(ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    authentication_classes = (JWTAuthentication,)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = (JWTAuthentication,)


class BookGenreViewSet(ModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = BookGenreSerializer
    authentication_classes = (JWTAuthentication,)

class HomePageTemplateView(TemplateView):
    template_name = 'index.html'
