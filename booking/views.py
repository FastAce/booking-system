from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Service, Booking, TimeSlot

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
    # Filter bookings for a specific user
    bookings = Booking.objects.all()  # Display all bookings for now
    return render(request, "booking/user_bookings.html", {"bookings": bookings})

# Form to manage TimeSlots
class TimeSlotForm(ModelForm):
    class Meta:
        model = TimeSlot
        fields = ["service", "date", "start_time", "end_time", "is_booked"]

# View to manage TimeSlots
def manage_time_slots(request):
    if request.method == "POST":
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_time_slots")
    else:
        form = TimeSlotForm()

    time_slots = TimeSlot.objects.all()
    return render(request, "booking/manage_time_slots.html", {"form": form, "time_slots": time_slots})
