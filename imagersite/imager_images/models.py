from django.db import models
from django.imager_profile import ImagerProfile
# Create your models here.


class Photo(models.Model):
    """."""


class Album(models.Model):
    """."""

    user = models.ForeignKey(ImagerProfile, related_name='album')
    photo = models.ManyToManyField(Photo)
    title = models.CharField(max_length=50)
