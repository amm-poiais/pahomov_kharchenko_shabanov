from django.db import models


class Dictionary(models.Model):
    """This class represents the dictionary model."""
    word = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=1023)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.word)

