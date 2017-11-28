from django.test import TestCase
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile, User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Create a new user from factory boy."""

    class Meta:
        """Meta class is used to change factory boy settings."""

        model = User
    username = 'bob'
    email = 'bob@bob.com'


class ProfileTests(TestCase):
    """Test class for testing profile model."""

    def setUp(self):
        """Set up fixture for testing."""
        self.user = UserFactory.create()
        self.user.set_password('test_pass')
        self.user.save()
        photo = Photo()
        album = Album()
        photo.user = self.user
        photo.title = 'Hello World'
        photo.description = 'My first photo'
        photo.image = 'http://cdn.spacetelescope.org/archives/images/screen/opo0328a.jpg'
        album.user = self.user
        album.title = 'Hello World Around the World'
        album.description = 'First Album'
        photo.save()
        album.save()

    def test_user_can_point_to_its_profile(self):
        """Test username is created."""
        # import pdb; pdb.set_trace()
        self.assertTrue(self.user.username == 'bob')