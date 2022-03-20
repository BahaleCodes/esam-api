from pickle import NONE
from pydoc import describe
from pyexpat import model
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from users.models import User

def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):

    class ArticleObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='Articles/default.jpg')
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=250)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_articles')
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    Articleobjects = ArticleObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
    
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#Album Model
class Album(models.Model):

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")
        ordering = ['-published']

    
    
    genre = models.ForeignKey(
    Genre, on_delete=models.DO_NOTHING, default=1)
    title = models.CharField(max_length=255, default=_(
        "New Album"), verbose_name=_("Album Title"))
    image = models.ImageField(
            _("Image"), upload_to=upload_to, default='cover-arts/default.jpg')
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='album_artist')
    artist = models.CharField(max_length=250)
    #Tracks
    tracks = []


    def __str__(self):
        return self.title




class Song(models.Model):
    options = (
        ('song', 'Song'),
        ('mixtape', 'Mixtape'),
    )
    genre = models.ForeignKey(
    Genre, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    song_file = models.FileField(_("Song"), upload_to=upload_to, max_length=100)
    image = models.ImageField(
            _("Image"), upload_to=upload_to, default='cover-arts/default.jpg')
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='song_artist')
    artist = models.CharField(max_length=250)
    song_type = models.CharField(
        max_length=10, choices=options, default='song')
    
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

class Album_Song(Song):
    album = models.ForeignKey(
        Album, related_name='album', on_delete=models.DO_NOTHING, null=True,default=NONE)
    


class Podcast_Episode(models.Model):

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    thumbnail = models.ImageField(
            _("Image"), upload_to=upload_to, default='pod-cast_pod/default.jpg')
    description = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(
            max_length=10, choices=options, default='published')
        
    
class Podcast(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(
            _("Image"), upload_to=upload_to, default='pod-cast_cover/default.jpg')
    description = models.TextField()
    episodes = models.ManyToManyField(Podcast_Episode)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='playlist/default.jpg')
    songs  = models.ManyToManyField(Song)

class ContentConsumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)


class Song_Stream(ContentConsumption):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email - super.song.title

class Article_Read(ContentConsumption):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email - super.article.title

class Pod_Stream(ContentConsumption):
    episode = models.ForeignKey("Podcast_Episode", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email - super.episode.title




