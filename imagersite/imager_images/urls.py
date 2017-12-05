from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^library/$', views.library_view, name='library'),
    url(r'^photos/$', views.photo_view, name='photos'),
    url(r'^albums/$', views.AlbumView.as_view(), name='albums'),
    url(r'^photos/(?P<pk>\d+)$', views.PhotoDetailView.as_view(), name='photo_details'),
    url(r'^albums/(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album_details'),
    url(r'^albums/add/$', views.NewAlbumView.as_view(), name='add_album'),
    url(r'^photos/add/$', views.NewPhotoView.as_view(), name='add_photo'),
    url(r'^photos/(?P<pk>\d+)/edit$', views.EditPhotoView.as_view(), name='edit_photo'),
    url(r'^albums/(?P<pk>\d+)/edit$', views.EditAlbumView.as_view(), name='edit_album')
]