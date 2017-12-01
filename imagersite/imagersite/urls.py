from django.conf.urls import include, url
from django.contrib import admin
from imager_profile import views
from django.conf.urls.static import static
from imagersite import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='home'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^profile/', include('imager_profile.urls')),
    url(r'^images/', include('imager_images.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )