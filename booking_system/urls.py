from django.contrib import admin
from django.urls import path, include
from booking.views_home import home  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("client/", include("booking.urls_client")),
    path("provider/", include("booking.urls_provider")),
    path("", home, name="home"),  # Home Page
]

