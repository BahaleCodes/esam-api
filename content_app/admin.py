from django.contrib import admin
from .models import Album, Album_Song, Playlist, Song_Stream,  Song, Article, Article_Read, Category, Genre

admin.site.register(Song_Stream)
admin.site.register(Song)
admin.site.register(Article)
admin.site.register(Article_Read)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Album_Song)
admin.site.register(Playlist)

