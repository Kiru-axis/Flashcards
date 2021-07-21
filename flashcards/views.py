from django.shortcuts import render,redirect
from .models import User,Course,FlashcardNotes
from .serializers import FlashcardNotesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
def index(request):
    return render(request,"flashcards/index.html")
def notes(request):
    print(notes)
    context ={
        "notes":FlashcardNotes.objects.all(),
        "subject": Course.objects.all(),
        "title": "Notes"
    }
    print(context)
    return render(request, 'flashcards/notes.html',context=context)

# serializers
class NotesList(APIView):
    def get(self,request,format=None):
        all_notes = FlashcardNotes.objects.all()
        serializers = FlashcardNotesSerializer(all_notes,many=True)
        print(all_notes)
        print(serializers)
        return Response(serializers.data)
        

