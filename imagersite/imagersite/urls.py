from django.conf.urls import include, url
from django.contrib import admin
from imager_profile import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='home'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]
