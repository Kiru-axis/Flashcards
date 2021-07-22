from django.contrib import admin
from .models import Course,Flashcard,Profile

# Register your models here.
admin.site.register(Course)
admin.site.register(Flashcard)
admin.site.register(Profile)

