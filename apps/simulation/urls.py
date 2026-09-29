from django.urls import path
from . import views

app_name = "simulation"

urlpatterns = [
    path("room/", views.immersive_room_view, name="immersive_room"),
    path("api/process_frame/", views.process_frame_api, name="process_frame"),
    path("api/end_session/", views.end_session_api, name="end_session"),
]
