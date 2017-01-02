from django.shortcuts import render
from .models import Limn, Album


def albums(request, id=None):
    paint = Album.objects.filter(type_id=id)
    context = {"paints": paint}
    return render(request, "gallery/albums.html", context)


def gallery(request):
    images = Limn.objects.filter(ty_pe_id=3)
    context = {"images": images}
    return render(request, "gallery/index.html", context)


def album(request, id=None):
    title_album = Album.objects.filter(id=id)
    images = Limn.objects.filter(album_id=id)
    context = {"images":images, "title_album":title_album}
    return render(request, "gallery/photos.html", context)