from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Album, Song, Artist, Comment
from django.contrib.auth.models import User
from .forms import CommentForm
import datetime


# Create your views here.
@login_required
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    print(context)
    for album in all_albums:
        print(album)
    return render(request, 'home/index.html', context=context)


@login_required
def album_detail(request, album_id):
    current_albums = Album.objects.filter(pk=album_id)
    current_album = Album.objects.get(pk=2)
    for alb in current_albums:
        current_album = alb
    all_songs = Song.objects.filter(song_album=album_id)

    context = {'all_songs': all_songs, 'current_album': current_album}
    return render(request, 'home/album_detail.html', context=context)


@login_required
def song_detail(request, song_id):
    current_song = Song.objects.get(pk=song_id)
    song_lines = current_song.song_lyrics.split("\\n")
    current_user = request.user
    print(current_user.id)
    now = datetime.datetime.now()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['comment_text'])

            new_comment = Comment(comment_text=form.cleaned_data['comment_text'],
                                  comment_user=current_user,
                                  comment_song=current_song,
                                  comment_datetime=str(now.strftime("%Y-%m-%d %H:%M")))
            new_comment.save()
            # from here insert in DB

    all_comments = Comment.objects.raw('SELECT * FROM homepage_comment WHERE comment_song_id=%s ORDER BY comment_datetime DESC'
                                       , [current_song.id])
    print(all_comments)
    context = {'current_song': current_song, 'song_lines': song_lines, 'all_comments': all_comments}

    return render(request, 'home/song_detail.html', context=context)


@login_required
def artist_detail(request, artist_id):
    current_artist = Artist.objects.get(pk=artist_id)
    print(current_artist)
    artist_songs = Song.objects.filter(song_artist_id=artist_id)
    print(artist_songs)
    context = {'current_artist': current_artist, 'artist_songs': artist_songs}
    return render(request, 'home/artist_detail.html', context)
