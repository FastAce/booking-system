from django.http import HttpResponse
from django.shortcuts import render
from .models import Service, Booking

# Home Page
def home(request):
    return HttpResponse("<h1>Welcome to the Booking System!</h1>")

# List of available services
def services_list(request):
    services = Service.objects.all()  # Retrieve all available services
    return render(request, "booking/services_list.html", {"services": services})

# Form to book a service
def book_service(request):
    if request.method == "POST":
        # Process form data here (placeholder for now)
        return HttpResponse("<h1>Reservation submitted successfully!</h1>")
    else:
        # Display the booking form
        return render(request, "booking/book_service.html", {})

# List of bookings for a user
def user_bookings(request):
    # Filter bookings for a specific user (placeholder for now)
    bookings = Booking.objects.all()  # Display all bookings
    return render(request, "booking/user_bookings.html", {"bookings": bookings})
