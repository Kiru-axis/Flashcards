from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("courses",views.CourseModelViewSet,basename="course")
router.register("flashcards",views.FlashcardModelViewSet,basename="flashcard")
router.register("users",views.UsersModelViewSet,basename="users")

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('api/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


