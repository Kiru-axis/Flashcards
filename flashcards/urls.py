from django.urls import path,include
from . import views
from rest_framework import routers

# modelviewsets need routers
router = routers.DefaultRouter()
# register the routers
router.register("courses",views.CourseModelViewSet,basename="course")
router.register("flashcards",views.FlashcardModelViewSet,basename="flashcard")
router.register("users",views.UsersModelViewSet,basename="users")

urlpatterns =[
    path('api/', include(router.urls)),
]