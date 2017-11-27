from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ImageActiveProfile(models.Manager):
    """Class to set user to active."""

    def get_queryset(self):
        """Create instance to set user active to true.."""
        return super(ImageActiveProfile, self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Create model for database."""

    active = ImageActiveProfile()

    @property
    def is_active(self):
        """Set is active as a property."""
        return self.user.is_active

    CAMERA_CHOICES = (
        ('NK', 'Nikon'),
        ('OL', 'Olympus'),
        ('GP', 'Go-Pro'),
    )
    SERVICE_CHOICES = (
        ('WD', 'Wedding'),
        ('GD', 'Graduation'),
        ('SP', 'Active/Sports'),
    )
    PHOTO_CHOICES = (
        ('BW', 'Black and White'),
        ('CL', 'Color')
    )
    website = models.URLField()
    location = models.CharField(max_length=100)
    fee = models.FloatField(blank=True, null=True)
    camera_type = models.CharField(
        max_length=2,
        choices=CAMERA_CHOICES,
        default='NK'
    )

    services = models.CharField(
        max_length=2,
        choices=SERVICE_CHOICES,
        default='WD'
    )
    bio = models.TextField()
    phone = models.CharField(max_length=100)
    photo_styles = models.CharField(
        max_length=2,
        choices=PHOTO_CHOICES,
        default='BW'
    )
    user = models.OneToOneField(User, related_name='profile')

