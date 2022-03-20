from .views import *
from django.urls import path

app_name = 'content'

urlpatterns = [
    #Article Urls
    path('articles/', ArticleList.as_view(), name='listArticle'),
    path('articles/last-read/', Last_read_articles.as_view(), name='listReadArticle'),
    path('article/<str:pk>/', ArticleDetail.as_view(), name='detailArticle'),
    path('article/search/', ArticleListDetailfilter.as_view(), name='searchArticle'),
    #Music
    path('albums/',GetAlbumsView.as_view(), name='getAlbums'),
    path('album/<str:pk>/',GetAlbumDetails.as_view(), name='getAlbums'),
    path('songs/', GetSongsView.as_view(), name='SongList'),
    path('song/<str:pk>/', ArticleDetail.as_view(), name='detailSong'),
    path('songs/last_sreamed/', Last_streamed_songs.as_view(), name='LastStreamedSongList'),
    path('song/search/', SongListDetailfilter.as_view(), name='searchSong'),
    path('song/create/',SongCreate.as_view(), name='createSong' ),
    path('songs/mixtapes/',GetLatestMixes.as_view(), name='getlatestmixes'),
    path('playlists/',GetPlaylists.as_view(),name="all-playlists"),
    path('playlists/<str:pk>/',GetPlaylistDetails.as_view(),name="all-playlists"),

    #Podcast
    path('podcast-episodes/', GetLatestEpisodesView.as_view(), name='episodeList'),
    path('podcast-episodes/last-viewed/', Last_viewed_pods.as_view(), name='episodelastViewedList'),
    #Others
    path('banner/', GetBannerContent.as_view(), name='banner'),


]