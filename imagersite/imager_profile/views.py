"""View module for home page and profile."""
import random
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .models import ImagerProfile


class HomeView(generic.ListView):
    """
    Hand the view for the home view.

    If user is logged in, one of their public photos will display,
    else a random users public photo will display.
    """

    model = ImagerProfile
    template_name = 'imagersite/home.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(HomeView, self).get_context_data(**kwargs)
        if context['view'].request.user.username:
            photos = context['view'].request.user.photo.all().filter(published='PUBLIC')
            rand = random.randint(0, len(photos) - 1)
            context['data'] = {
                'photo': photos[rand]
            }
        else:
            photo = False
            while not photo:
                users = context['data']
                ran_user = random.randint(0, len(users) - 1)
                user = users[ran_user]
                if user.user.photo.all().filter(published='PUBLIC'):
                    photos = user.user.photo.all().filter(published='PUBLIC')
                    rand = random.randint(0, len(photos) - 1)
                    photo = photos[rand]
                    context['data'] = {
                        'photo': photo
                    }

        return context


class ProfileView(generic.ListView):
    """."""

    model = ImagerProfile
    template_name = 'imager_profile/profile.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        """."""
        context = super(ProfileView, self).get_context_data(**kwargs)
        if self.kwargs:
            users = context['data']
            profile = ''
            for user in users:
                if user.user.username == self.kwargs['slug']:
                    profile = user
            context['data'] = {
                'username': profile.user.username,
                'num_photos': profile.user.photo.all().count(),
                'num_albums': profile.user.album.all().count(),
                'camera_type': profile.user.profile.camera_type,
                'fee': profile.user.profile.fee,
                'website': profile.user.profile.website,
                'services': profile.user.profile.services,
                'bio': profile.user.profile.bio
            }
        else:
            user = context['view'].request.user
            context['data'] = {
                'username': user.username,
                'num_photos': user.photo.all().count(),
                'num_albums': user.album.all().count(),
                'camera_type': user.profile.camera_type,
                'fee': user.profile.fee,
                'website': user.profile.website,
                'location': user.profile.location,
                'services': user.profile.services,
                'bio': user.profile.bio,
                'phone': user.profile.phone,
                'is_active': user.profile.is_active,
            }
        return context


class UpdateProfile(generic.UpdateView):
    """."""

    model = ImagerProfile
    template_name = 'imager_profile/update_profile.html'
    fields = ['website', 'fee', 'camera_type', 'services', 'bio', 'phone', 'photo_styles']
    success_url = reverse_lazy('library')


