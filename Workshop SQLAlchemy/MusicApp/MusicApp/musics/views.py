from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'common/index.html')


def create_album(request):
    return render(request, 'albums/create-album.html')


def edit_album(request):
    return render(request, 'albums/edit-album.html')


def delete_album(request):
    return render(request, 'albums/delete-album.html')


def album_details(request):
    return render(request, 'albums/album-details.html')


def create_song(request):
    return render(request, 'songs/create-song.html')
