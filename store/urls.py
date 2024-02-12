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
    path(
        "category/<str:foo>", views.category, name="category"
    ),  # Str = string / foo = variable passed in
    path(
        "category_summary", views.category_summary, name="category_summary"
    ),  # Str = string / foo = variable passed in
    path("update_user/", views.update_user, name="update_user"),
    path("update_password/", views.update_password, name="update_password"),
]
