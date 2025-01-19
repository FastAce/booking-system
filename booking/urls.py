from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Page d'accueil
    path("services/", views.services_list, name="services_list"),  # Liste des services
    path("book/", views.book_service, name="book_service"),  # Formulaire de réservation
    path("my-bookings/", views.user_bookings, name="user_bookings"),  # Réservations utilisateur
]

