from django.db import models
from django.contrib.auth.models import User, UserManager


class Dictionary(models.Model):
    """This class represents the dictionary model."""
    word = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=1023)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.word)


class CustomUser(User):
    """User with app settings."""
    history_words = models.ManyToManyField(Dictionary, related_name='history_words')
    favorite_words = models.ManyToManyField(Dictionary, related_name='favorite_words')

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()
