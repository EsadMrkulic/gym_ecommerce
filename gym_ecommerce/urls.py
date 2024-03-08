from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("store.urls")),  # Including a new URL that leads to the store app
    path("cart/", include("cart.urls")),  # Including a URL that leads to the cart app
    path("payment/", include("payment.urls")),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)  # To allow image upload
