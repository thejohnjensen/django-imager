from django.shortcuts import render


def library_view(request):
    """."""
    DATA = {
        'albums': request.user.album.all(),
        'photos': request.user.photo.all(),
    }
    return render(request, 'imager_images/library.html', {'data': DATA})


def photo_view(request):
    """."""
    DATA = {
        'photos': request.user.photo.all().filter(published='PUBLIC')
    }
    return render(request, 'imager_images/photos.html', {'data': DATA})


def album_view(request):
    """."""

    DATA = {
        'albums': request.user.album.all().filter(published='PUBLIC'),
    }
    return render(request, 'imager_images/albums.html', {'data': DATA})


def photo_details(request, id):
    """."""
    photo = request.user.photo.get(id=id)
    return render(request, 'imager_images/photo_details.html', {'photo': photo})


def album_details(request, id):
    """."""
    # import pdb; pdb.set_trace()
    DATA = {
        'photos': request.user.album.get(id=id).photos.all()
    }
    return render(request, 'imager_images/album_details.html', {'data': DATA})