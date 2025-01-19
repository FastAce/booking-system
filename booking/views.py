from django.http import HttpResponse
from django.shortcuts import render
from .models import Service

# Vue pour la page d'accueil
def home(request):
    return HttpResponse("<h1>Welcome to the Booking System!</h1>")

# Vue pour afficher la liste des services
def services_list(request):
    services = Service.objects.all()  # Récupère tous les services disponibles
    return render(request, "booking/services_list.html", {"services": services})

# Vue pour afficher un formulaire de réservation (placeholder pour l'instant)
def book_service(request):
    return HttpResponse("<h1>Reservation form will be here!</h1>")


