from django.db import models
from datetime import datetime, timedelta

# Modèle pour les prestations
class Service(models.Model):
    name = models.CharField(max_length=100)  # Nom de la prestation
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix

    def __str__(self):
        return self.name

# Modèle pour les réservations
class Booking(models.Model):
    client_name = models.CharField(max_length=100)  # Nom du client
    client_email = models.EmailField()  # Email du client
    services = models.ManyToManyField(Service)  # Plusieurs prestations possibles
    date = models.DateField()  # Date de la réservation
    time = models.TimeField()  # Heure de la réservation
    is_canceled = models.BooleanField(default=False)  # Statut d'annulation

    def __str__(self):
        service_names = ', '.join([service.name for service in self.services.all()])
        return f"{self.client_name} - {service_names} ({self.date} {self.time})"

    def total_price(self):
        """Calcule le prix total des prestations dans la réservation"""
        return sum(service.price for service in self.services.all())

    def can_be_canceled(self):
        """Vérifie si la réservation peut encore être annulée (jusqu'à 24h avant)"""
        now = datetime.now()
        booking_datetime = datetime.combine(self.date, self.time)
        return booking_datetime - now > timedelta(hours=24)

