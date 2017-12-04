from django.test import TestCase
from django.contrib.auth.models import User
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile
import factory


class PhotoFactory(factory.django.DjangoModelFactory):
    """Create a new photo from factory boy."""

    class Meta:
        """Meta class is used to change factory boy settings."""

        model = Photo
    title = factory.Sequence(lambda n: f'photo{n}')


class ProfileTests(TestCase):
    """Test class for testing profile model."""

    def setUp(self):
        """Set up fixture for testing."""
        user = User(username='bob', email='bob@bob.com')
        user.set_password('test_pass')
        user.save()
        album = Album()
        album.id = 0
        album.user = user
        album.title = 'Hello World Around the World'
        album.description = 'First Album'
        for _ in range(10):
            photo = PhotoFactory.build()
            photo.user = user
            photo.description = 'My {} photo'.format(_)
            photo.image = 'http://cdn.spacetelescope.org/archives/images/screen/opo0328a.jpg'
            photo.save()
            album.photos.add(photo)
        album.save()

    def test_user_has_photo(self):
        """Test user has photo."""
        user = User.objects.first()
        self.assertTrue(user.photo.first().description == 'My 0 photo')
       

    def test_user_has_album(self):
        """Test user has album."""
        user = User.objects.first()
        self.assertTrue(user.album.first().title == 'Hello World Around the World')
        self.assertTrue(user.album.first().description == 'First Album')

    def test_user_has_10_photos(self):
        """Test user has 10 photos."""
        user = User.objects.first()
        self.assertTrue(user.photo.count() == 10)