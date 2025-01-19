from django.urls import path
from . import views  

urlpatterns = [
    path("", views.home, name="home"),  # Home Page
    path("services/", views.services_list, name="services_list"),  # List of services
    path("book/", views.book_service, name="book_service"),  # Name of services
]

