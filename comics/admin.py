from django.contrib import admin
from comics.models import Comics, Genre, Artist, Publisher, Article, Kind

admin.site.register(Comics)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Publisher)
admin.site.register(Article)
admin.site.register(Kind)
