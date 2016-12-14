from django.shortcuts import render
from .models import Limn,Type, Album


def get_photos():
    photo_albums = Album.objects.filter(type_id=1)
    return {"photos": photo_albums}


def get_paints():
    paint_albums = Album.objects.filter(type_id=2)
    return {"paints": paint_albums}


def gallery(request):
    images = Limn.objects.all()
    context = {"images": images}
#    context.update(get_photos())
#    context.update(get_paints())
    return render(request, "gallery/index.html", context)

def album_single(request):
    images = Limn.objects.filter(album__type_id=1)
    context = {"images":images}
    return render(request, "gallery/photos.html", context)

def album_two(request):
    images = Limn.objects.filter(album__type_id=2)
    context = {"images": images}
    return render(request, "gallery/album_two.html", context)


def upload(request):
    return render(request,"gallery/upload.html")