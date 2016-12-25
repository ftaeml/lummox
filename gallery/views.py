from django.shortcuts import render
from .models import Limn, Album


def albums(request, id=None):
    paint = Album.objects.filter(type_id=id)
    context = {"paints": paint}
    return render(request, "gallery/albums.html", context)


def gallery(request):
    images = Limn.objects.filter(album_id=1)
    context = {"images": images}
    return render(request, "gallery/index.html", context)


def album(request, id=None):
    images = Limn.objects.filter(album_id=id)
    context = {"images":images}
    return render(request, "gallery/photos.html", context)