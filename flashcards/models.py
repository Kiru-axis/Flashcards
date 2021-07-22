from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

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
