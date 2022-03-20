
from rest_framework import serializers
from .models import *
from users.serializers import CustomUserSerializer


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class AlbumSerializer(serializers.ModelSerializer):
    genre = GenreSerializers()
    class Meta:
        model = Album
        fields = '__all__'


class LastViewedPodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pod_Stream
        fields = '__all__'

class LastReadArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_Read
        fields = '__all__'

class LastSongStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song_Stream
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = CustomUserSerializer()
    class Meta:
        model = Article
        fields = '__all__'

class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields =  '__all__'

class PlaylistDetailSerializers(serializers.ModelSerializer):
    songs = SongSerializers(read_only=True, many=True)
    class Meta:
        model =  Playlist
        fields = '__all__'


class PlaylistsListSerializers(serializers.ModelSerializer):
  
    class Meta:
        model =  Playlist
        fields = [ "title","image"]


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

class PodEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast_Episode
        fields = '__all__'

class SongStreamSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Song_Stream
        fields =  '__all__'

class PodStreamSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Pod_Stream
        fields =  '__all__'

class ArticleReadSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Article
        fields =  '__all__'

class AlbumSongSerializer(serializers.ModelSerializer):

    album = AlbumSerializer(read_only=True)

    class Meta:
    
        model = Album_Song
        fields = '__all__'