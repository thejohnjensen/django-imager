"""Handle the views for photo and album models."""
from .models import Photo, Album
from django.views import generic
from django.core.urlresolvers import reverse_lazy


class LibraryView(generic.ListView):
    """View for the library page."""

    model = Photo
    template_name = 'imager_images/library.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(LibraryView, self).get_context_data(**kwargs)
        context['data'] = {
            'albums': context['view'].request.user.album.all(),
            'photos': context['view'].request.user.photo.all()
        }
        return context


class PhotoView(generic.ListView):
    """Display all the users public photos on the photos page."""

    model = Photo
    template_name = 'imager_images/photos.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['data'] = context['view'].request.user.photo.all()
        return context


class AlbumView(generic.ListView):
    """View for the album page for users albums."""

    model = Album
    template_name = 'imager_images/albums.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(AlbumView, self).get_context_data(**kwargs)
        context['data'] = context['view'].request.user.album.all()
        return context


class PhotoDetailView(generic.DetailView):
    """View for single photo, can edit from this page."""

    model = Photo
    template_name = 'imager_images/photo_details.html'


class AlbumDetailView(generic.DetailView):
    """View for single album, can edit from this page."""

    model = Album
    template_name = 'imager_images/album_details.html'
    context_object_name = 'data'


class NewPhotoView(generic.CreateView):
    """View to add a new photo."""

    model = Photo
    template_name = 'imager_images/new_photo.html'
    fields = ['user', 'image', 'title', 'description', 'published']
    success_url = reverse_lazy('library')


class NewAlbumView(generic.CreateView):
    """View to add a new album."""

    model = Album
    template_name = 'imager_images/new_album.html'
    fields = ['user', 'photos', 'title', 'description', 'cover', 'published']
    success_url = reverse_lazy('library')


class EditPhotoView(generic.UpdateView):
    """View to edit photo."""

    model = Photo
    template_name = 'imager_images/edit_photo.html'
    fields = ['user', 'image', 'title', 'description', 'published']
    success_url = reverse_lazy('library')


class EditAlbumView(generic.UpdateView):
    """View to add album."""

    model = Album
    template_name = 'imager_images/edit_album.html'
    fields = ['user', 'photos', 'title', 'description', 'cover', 'published']
    success_url = reverse_lazy('library')
