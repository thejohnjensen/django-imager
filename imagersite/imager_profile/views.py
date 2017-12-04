from django.shortcuts import render
from django.contrib.auth.models import User
import random
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import ImagerProfile


def home_view(request):
    """."""
    images = request.user.photo.all()
    random_pic = images[random.randint(0, len(images) - 1)]
    return render(request, 'imagersite/home.html', {'image': random_pic})


def profile_view(request):
    """."""
    DATA = {
        'num_photos': request.user.photo.all().count(),
        'num_albums': request.user.album.all().count(),
        'camera_type': request.user.profile.camera_type,
        'fee': request.user.profile.fee,
        'website': request.user.profile.website,
        'location': request.user.profile.location,
        'services': request.user.profile.services,
        'bio': request.user.profile.bio,
        'phone': request.user.profile.phone,
        'is_active': request.user.profile.is_active,
        'username': request.user.username,
        'pk': request.user.pk

    }
    return render(request, 'imager_profile/profile.html', {'DATA': DATA})


def profile_visit(request):
    """."""
    username = request.path.split('/')[-1]
    if User.objects.get(username=username):
        DATA = {
            'num_photos': request.user.photo.all().count(),
            'num_albums': request.user.album.all().count(),
            'camera_type': request.user.profile.camera_type,
            'fee': request.user.profile.fee,
            'website': request.user.profile.website,
            'location': request.user.profile.location,
            'services': request.user.profile.services,
            'bio': request.user.profile.bio,
            'phone': request.user.profile.phone
        }
        return render(request, 'imager_profile/profile.html', {'DATA': DATA})


class UpdateProfile(generic.UpdateView):
    """."""
    model = ImagerProfile
    template_name = 'imager_profile/update_profile.html'
    fields = ['website', 'fee', 'camera_type', 'services', 'bio', 'phone', 'photo_styles']
    success_url = reverse_lazy('library')


