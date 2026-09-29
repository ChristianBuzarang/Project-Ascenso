from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("api/chart_data/", views.chart_data_api, name="chart_data"),
]
