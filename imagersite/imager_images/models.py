from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    """Model for adding photos."""

    user = models.ForeignKey(User, related_name='photo', on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public')
    ]
    published = models.CharField(
        max_length=10,
        choices=PUBLISHED,
        default='PRIVATE'
    )

    def __str__(self):
        return 'Photo by {}.'.format(self.user.username)


class Album(models.Model):
    """Model for adding photo albums."""

    user = models.ForeignKey(User, related_name='album', on_delete=models.CASCADE)
    photos = models.ManyToManyField(Photo)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public')
    ]
    published = models.CharField(
        max_length=10,
        choices=PUBLISHED,
        default='PRIVATE'
    )

    def __str__(self):
        return 'Album by {}.'.format(self.user.username)