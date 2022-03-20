from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('profiles/',Profile_list.as_view(), name="get_artists_profiles"),
    path('profile/', UserDetail.as_view(), name='detailArticle'),
    

]
