from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),  # URL for the homepage
    path("about/", views.about, name="about"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path(
        "product/<int:pk>", views.product, name="product"
    ),  # Int = integer / pk = primary key
]
