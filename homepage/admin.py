from django.contrib import admin
from .models import Album, Artist, Song, Comment

# Register your models here.


admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Comment)
