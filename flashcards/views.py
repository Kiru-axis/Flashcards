from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProfileSerializer
from rest_framework import status
from .models import Profile
from rest_framework.exceptions import AuthenticationFailed


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


        payload = {
            'id': profile.id,
            'exp' : datetime.datetime.utcnow()
        }

        return Response({
            'message': "You have loged in successfully"
        })
