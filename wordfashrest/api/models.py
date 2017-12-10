from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Dictionary(models.Model):
    """This class represents the dictionary model."""
    word = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=1023)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.word)


class Profile(models.Model):
    """User with app settings."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    history_words = models.ManyToManyField(Dictionary, related_name='history_words')
    favorite_words = models.ManyToManyField(Dictionary, related_name='favorite_words')

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.user.username,
                           self.user.password)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
