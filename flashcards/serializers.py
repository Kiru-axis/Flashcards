from rest_framework import serializers
from .models import Course,FlashcardNotes

class FlashcardNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashcardNotes
        fields=("title","user","date","courses")
        