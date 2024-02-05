from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),  # URL for the homepage
    path("about/", views.about, name="about"),
]
