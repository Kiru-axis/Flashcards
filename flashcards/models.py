from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Course(models.Model):
    subject=models.CharField(max_length=50)

    def __str__(self):
        return self.subject
class FlashcardNotes(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,related_name="flashcardsnotes")
    date = models.DateField(default=timezone.now)
    description=models.TextField(blank=True)
    courses=models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course')

    # save flashcardsnotes
    def save_flashcardnotes(self):
        self.save()
    # delete flashcardnotes
    def delete_flashcardnotes(self):
        self.delete()
    # update notes
    @classmethod 
    def update_notes(self,cls):
        pass


    def __str__(self):
        return f"{self.user.username}  {self.title} {self.description} {self.courses.subject}"
