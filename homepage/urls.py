from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.album_detail, name='album_detail'),
    url(r'^song/(?P<song_id>[0-9]+)/$', views.song_detail, name='song_detail'),
    url(r'^artist/(?P<artist_id>[0-9]+)/$', views.artist_detail, name='artist_detail'),
]
