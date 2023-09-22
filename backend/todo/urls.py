from django.urls import path
from .views import *

urlpatterns = [
    path("todo/", TodoListCreate.as_view()),
    path("edit/<str:pk>/", TodoUpdateDelete.as_view()),
    path("users/", RandomUsers.as_view()),
]
