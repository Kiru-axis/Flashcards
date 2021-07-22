from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(AbstractUser):
    user = models.CharField(max_length=255)
    bio = models.TextField(max_length=500, blank=True)
    profile_photo = models.ImageField(upload_to="images/")
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=AbstractUser)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=AbstractUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

