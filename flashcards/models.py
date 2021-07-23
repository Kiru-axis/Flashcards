from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings

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


class Course(models.Model):
    subject=models.CharField(max_length=50)

    def __str__(self):
        return self.subject
        
class Flashcard(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="flashcards")
    date = models.DateTimeField()
    description=models.TextField(blank=True)
    courses=models.ForeignKey(Course, on_delete=models.CASCADE,related_name='courses')

    def __str__(self):
        return f"{self.user.username} ({self.date}) ({self.courses.subject})"

