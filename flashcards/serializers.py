from django.db.models import fields
from rest_framework import serializers
from .models import Course,Flashcard,Profile
from django.contrib.auth.models import User

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields = ("id","subject")
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ("id","username")

# who is accessing the endpoints
class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ("username",)
        read_only = fields

class FlashcardSerializer(serializers.ModelSerializer):
    courses = serializers.SlugRelatedField(slug_field="subject",queryset=Course.objects.all())
    user = ReadUserSerializer()
    class Meta:
        model = Flashcard
        fields = ("id","title","date", "description", "courses","user",)
        # fields =" __all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
