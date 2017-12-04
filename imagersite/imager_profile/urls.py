from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.profile_view, name='profile'),
    url(r'^\w+$', views.profile_visit, name='visit_profile'),
    url(r'^edit/(?P<pk>\d+)$', views.UpdateProfile.as_view(), name='update_profile')
]
