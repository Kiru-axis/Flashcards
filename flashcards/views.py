from django.shortcuts import render,redirect
from .models import User,Course,FlashcardNotes
from .serializers import FlashcardNotesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

    # post request
    def post(self,request,**kwargs):
        serializers = FlashcardNotesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            print(serializers)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)
        pass        

