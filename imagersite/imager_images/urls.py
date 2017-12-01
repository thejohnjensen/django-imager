from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^library/$', views.library_view, name='library'),
    url(r'^photos/$', views.photo_view, name='photos'),
    url(r'^albums/$', views.album_view, name='albums'),
    url(r'^photos/(?P<id>\d+)$', views.photo_details, name='photo_details'),
    url(r'^albums/(?P<id>\d+)$', views.album_details, name='album_details')
]