from django.shortcuts import render
from .models import Photo, Album
from django.views import generic
from django.core.urlresolvers import reverse_lazy


def library_view(request):
    """."""
    data = {
        'albums': request.user.album.all(),
        'photos': request.user.photo.all(),
    }
    return render(request, 'imager_images/library.html', {'data': data})


def photo_view(request):
    """."""
    data = {
        'photos': request.user.photo.all().filter(published='PUBLIC')
    }
    return render(request, 'imager_images/photos.html', {'data': data})


class AlbumView(generic.ListView):
    """."""

    model = Album
    template_name = 'imager_images/albums.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(AlbumView, self).get_context_data(**kwargs)
        context['data'] = context['view'].request.user.album.all()
        return context


class PhotoDetailView(generic.DetailView):
    """."""

    model = Photo
    template_name = 'imager_images/photo_details.html'


class AlbumDetailView(generic.DetailView):
    """."""

    model = Album
    template_name = 'imager_images/album_details.html'
    context_object_name = 'data'


class NewPhotoView(generic.CreateView):
    """."""

    model = Photo
    template_name = 'imager_images/new_photo.html'
    fields = ['user', 'image', 'title', 'description', 'published']
    success_url = reverse_lazy('library')


class NewAlbumView(generic.CreateView):
    """."""

    model = Album
    template_name = 'imager_images/new_album.html'
    fields = ['user', 'photos', 'title', 'description', 'cover', 'published']
    success_url = reverse_lazy('library')


class EditPhotoView(generic.UpdateView):
    """."""

    model = Photo
    template_name = 'imager_images/edit_photo.html'
    fields = ['user', 'image', 'title', 'description', 'published']
    success_url = reverse_lazy('library')


class EditAlbumView(generic.UpdateView):
    """."""

    model = Album
    template_name = 'imager_images/edit_album.html'
    fields = ['user', 'photos', 'title', 'description', 'cover', 'published']
    success_url = reverse_lazy('library')
