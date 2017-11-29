from django.test import TestCase
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

    def test_user_can_point_to_its_profile(self):
        """Test user has profile."""
        self.assertIsNotNone(self.user.profile)

    def test_user_field_username(self):
        """Test username is created."""
        self.assertTrue(self.user.username == 'bob')

    def test_user_field_password(self):
        """Test that password checks out."""
        self.assertTrue(self.user.check_password('test_pass'))

    def test_user_camera_type(self):
        """Test that the default camera type is Nikon."""
        self.assertTrue(self.user.profile.camera_type == 'NK')

    def test_user_is_active(self):
        """Test that the user is active."""
        self.assertTrue(self.user.profile.is_active)

    def test_user_services_default(self):
        """Test that the user default is wedding."""
        self.assertTrue(self.user.profile.services == 'WD')

    def test_user_photo_styles_default(self):
        """Test default photo style is black and white."""
        self.assertTrue(self.user.profile.photo_styles == 'BW')

    def test_user_change_photo_style(self):
        """Test that photo style can be changed to color."""
        self.user.profile.photo_styles = 'CL'
        self.assertTrue(self.user.profile.photo_styles == 'CL')

    def test_getting_user_by_id(self):
        """Test getting user by id."""
        user_one = User.objects.get()
        self.assertTrue(user_one.username == 'bob')

    def test_user_profile_has_url_field(self):
        """Test user has URL Field."""
        self.assertIsNotNone(self.user.profile.website)

    def test_user_profile_has_location(self):
        """Test user has location."""
        self.assertIsNotNone(self.user.profile.location)

    def test_user_profile_has_fee(self):
        """Test user has location."""
        self.assertIsNone(self.user.profile.fee)

    def test_user_profile_has_phone_number(self):
        """Test user has location."""
        self.assertIsNotNone(self.user.profile.phone)

    def test_user_profile_has_bio(self):
        """Test user has location."""
        self.assertIsNotNone(self.user.profile.bio)
