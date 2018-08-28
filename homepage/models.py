from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Album(models.Model):
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    album_desc = models.CharField(max_length=500)

    def __str__(self):
        return self.album_title


class Artist(models.Model):
    artist_name = models.CharField(max_length=500)
    artist_image = models.CharField(max_length=1000)
    artist_desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.artist_name


class Song(models.Model):
    song_title = models.CharField(max_length=500)
    song_path = models.CharField(max_length=1000)
    song_length = models.CharField(max_length=100)
    song_lyrics = models.CharField(max_length=10000)
    song_image = models.CharField(max_length=1000)
    song_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_title


class Comment(models.Model):
    comment_text = models.CharField(max_length=1000)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_song = models.ForeignKey(Song, on_delete=models.CASCADE)
    comment_datetime = models.CharField(max_length=1000, default='16 Aug, 16:48')

    def __str__(self):
        return self.comment_text
