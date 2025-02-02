from django.db import models
from datetime import datetime, timedelta
from django.forms import ModelForm  # ✅ Importation of form

# Model for services
class Service(models.Model):
    name = models.CharField(max_length=100)  # Service name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Service price

    def __str__(self):
        return self.name

# Model for available time slots
class TimeSlot(models.Model):
    provider = models.CharField(max_length=100)  # Provider's name
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Related service
    date = models.DateField()  # Date of the time slot
    start_time = models.TimeField()  # Start time of the time slot
    end_time = models.TimeField()  # End time of the time slot
    is_booked = models.BooleanField(default=False)  # Indicates if the time slot is booked

    def __str__(self):
        return f"{self.provider}: {self.service.name} on {self.date} ({self.start_time}-{self.end_time})"

# Model for bookings
class Booking(models.Model):
    client_name = models.CharField(max_length=100)  
    client_email = models.EmailField()  
    services = models.ManyToManyField(Service)  
    date = models.DateField()  
    time = models.TimeField()  
    is_canceled = models.BooleanField(default=False)  
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True, blank=True)  # ✅ NULL values

    def __str__(self):
        service_names = ', '.join([service.name for service in self.services.all()])
        return f"{self.client_name} - {service_names} ({self.time_slot.date} {self.time_slot.start_time})"

    def total_price(self):
        """Calculate the total price of the services in the booking"""
        return sum(service.price for service in self.services.all())

    def can_be_canceled(self):
        """Check if the booking can still be canceled (up to 24 hours before)"""
        now = datetime.now()
        booking_datetime = datetime.combine(self.time_slot.date, self.time_slot.start_time)
        return booking_datetime - now > timedelta(hours=24)

# ✅ Form for Booking and TimeSlot
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["client_name", "client_email", "services", "time_slot"]

class TimeSlotForm(ModelForm):
    class Meta:
        model = TimeSlot
        fields = ["provider", "service", "date", "start_time", "end_time"]

