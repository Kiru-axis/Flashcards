from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .models import Flashcard,Course,Profile
from .serializers import CourseSerializer,FlashcardSerializer,UserSerializer,ProfileSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"flashcards/index.html")

class RegisterView(APIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        profile = Profile.objects.filter(email=email).first()

        if profile is None:
            raise AuthenticationFailed('Profile not found')

        if not profile.check_password(password):
            raise AuthenticationFailed('incorrect password')

        return Response({
            'message': "You have loged in successfully"
        })


# viewsets to expose all http verbs for saving and deletion
class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    print(queryset)

# Users serializers and models
class UsersModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    print(queryset)


# Flashcards serializers and models
class FlashcardModelViewSet(ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    print(queryset)

