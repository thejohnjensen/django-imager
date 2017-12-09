from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ProfileView.as_view(), name='profile'),
    url(r'^(?P<slug>\w+)$', views.ProfileView.as_view(), name='visit_profile'),
    url(r'^edit/(?P<pk>\d+)$', views.UpdateProfile.as_view(), name='update_profile')
]
