from django.shortcuts import render
from .models import Flashcard,Course
from .serializers import CourseSerializer,FlashcardSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .permissions import IsAdminOrReadOnly
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
    permision_classes = (IsAdminOrReadOnly,)
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    print(queryset)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        # return super().perform_create(serializer)