from django.contrib import admin

from apps.book.models import Book, BookGenre, BookCategory

admin.site.register([Book, BookGenre, BookCategory])
