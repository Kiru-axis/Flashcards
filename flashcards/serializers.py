from rest_framework import serializers
from .models import Course,Flashcard
from django.contrib.auth.models import User

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = ("id","subject")
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ("id","username")

class FlashcardSerializer(serializers.ModelSerializer):
    courses = serializers.SlugRelatedField(slug_field="subject",queryset=Course.objects.all())
    class Meta:
        model = Flashcard
        fields = ( "id","title", "user", "date", "description", "courses")
