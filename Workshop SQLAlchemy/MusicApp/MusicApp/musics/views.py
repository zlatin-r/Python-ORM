from django.shortcuts import render, redirect

from MusicApp.common.session_decorator import session_decorator
from MusicApp.musics.forms import SongCreateForm, AlbumCreateForm
from MusicApp.musics.models import Album
from MusicApp.settings import session


# Create your views here.

@session_decorator(session)
def index(request):
    albums = session.query(Album).all()

    context = {
        'albums': albums
    }

    return render(request, 'common/index.html', context)


def create_album(request):
    if request.method == "GET":
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
    }

    return render(request, 'albums/create-album.html', context)


def edit_album(request, pk: int):
    return render(request, 'albums/edit-album.html')


def delete_album(request, pk: int):
    return render(request, 'albums/delete-album.html')


@session_decorator(session)
def album_details(request, pk: int):
    album = (session.query(Album)
                    .filter_by(id=pk)
                    .first()
             )

    contex = {
        'album': album
    }

    return render(request, 'albums/album-details.html', contex)


def create_song(request):
    if request.method == "GET":
        form = SongCreateForm()
    else:
        form = SongCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
    }

    return render(request, 'songs/create-song.html', context)
