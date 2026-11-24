from django.urls import path
from . import views

app_name = "user_profile"

urlpatterns = [
    path("", views.profile_view, name="profile"),
    path("connect/", views.connect_view, name="connect"),
    path("assignment/", views.assignment_view, name="assignment"),
]

