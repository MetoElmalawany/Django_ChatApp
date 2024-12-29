from django.urls import path
from .views import RegisterPage
from . import views


urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<str:slug>", views.room, name="room"),
    path('register/', RegisterPage.as_view(), name='register'),
]