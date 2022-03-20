from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
# Display Posts


class GetBannerContent(APIView):
    def get_article_queryset(self):
        queryset = Article.objects.all().order_by('-published')[0]
        return queryset
    
    def get_podEpisode_queryset(self):
        queryset = Podcast_Episode.objects.all().order_by('-published')[0]
        return queryset


    def get(self, request, format=None):
        try:
            user = request.user
            print(user)
            articles = Article_Read.objects.filter(user=user)
            pods = Pod_Stream.objects.filter(user=user)
            #Check which does the user consume the most
            if pods.count > articles.count:
                content =  self.get_podEpisode_queryset()
                serializer = PodEpisodeSerializer(content)
        except:
            article =  Article.objects.all().order_by('-published')[0]
            serializer = ArticleSerializer(article)
       
        return Response(serializer.data,  status=status.HTTP_200_OK)



class Last_viewed_pods(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LastViewedPodSerializer
    queryset = Pod_Stream.objects.all().order_by('-date_time')[:10]


class Last_streamed_songs(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LastSongStreamSerializer
    queryset = Song_Stream.objects.all().order_by('-date_time')[:10]


class Last_read_articles(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LastReadArticleSerializer
    queryset = Article_Read.objects.all().order_by('-date_time')[:10]


class ArticleList(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleListDetailfilter(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']



class GetLatestEpisodesView(APIView):
    serializer_class = PodEpisodeSerializer

    def get_queryset(self):
        queryset = Podcast_Episode.objects.order_by('published')[:10]
        return queryset


    def get(self, request, format=None):
        try:
            id = request.query_params["id"]
            episode = Podcast_Episode.objects.get(id=id)
            serializer = SongSerializers(episode)
        except:
            episodes =  self.get_queryset()
            serializer = SongSerializers(episodes, many=True)

        return Response(serializer.data,  status=status.HTTP_200_OK)


class GetSongsView(APIView):
    serializer_class = SongSerializers
    
    def get_queryset(self):
        queryset = Song.objects.all()
        return queryset

    def get(self, request, format=None):
        try:
            id = request.query_params["id"]
            song = Song.objects.get(id=id)
            serializer = SongSerializers(song)
        except:
            songs =  self.get_queryset()
            serializer = SongSerializers(songs, many=True)
        
        return Response(serializer.data,  status=status.HTTP_200_OK)



class GetLatestMixes(APIView):
    serializer_class = SongSerializers
    
    def get_queryset(self):
        queryset = Song.objects.filter(song_type='mixtape')
        return queryset

    def get(self, request, format=None):
        mixes =  self.get_queryset()
        serializer = SongSerializers(mixes, many=True)
        
        return Response(serializer.data,  status=status.HTTP_200_OK)

class GetPlaylists(generics.ListAPIView):
    serializer_class = PlaylistsListSerializers
    queryset =  Playlist.objects.all();

class GetAlbumsView(generics.ListAPIView):
    serializer_class = AlbumSerializer
    queryset =  Album.objects.all();


class GetAlbumDetails(APIView):

    def get(self, request, format=None, **kwargs):
        album_songs = Album_Song.objects.filter(album=kwargs['pk'])
        serializer = AlbumSongSerializer(album_songs, many=True)
        return Response(serializer.data)

class GetPlaylistDetails(APIView):

    def get(self, request, format=None, **kwargs):
        playlist = Playlist.objects.filter(id=kwargs['pk'])
        serializer = PlaylistDetailSerializers(playlist, many=True)
        return Response(serializer.data)



class SongCreate(APIView):

    def post(self, request, format=None):
        print(request.data)
        serializer = SongSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SongListDetailfilter(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = SongSerializers
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']
