from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Service, Booking, TimeSlot

# Home Page
def home(request):
    # Render the home page
    return render(request, "booking/home.html")

# List of available services
def services_list(request):
    # Retrieve all available services from the database
    services = Service.objects.all()
    return render(request, "booking/services_list.html", {"services": services})

# Form to book a service
def book_service(request):
    if request.method == "POST":
        # Placeholder for form processing logic
        return HttpResponse("<h1>Reservation submitted successfully!</h1>")
    else:
        # Render the booking form
        return render(request, "booking/book_service.html", {})

# List of bookings for a user
def user_bookings(request):
    # Retrieve all bookings from the database
    bookings = Booking.objects.all()
    return render(request, "booking/user_bookings.html", {"bookings": bookings})

# Form to manage time slots
class TimeSlotForm(ModelForm):
    class Meta:
        model = TimeSlot
        fields = ["service", "date", "start_time", "end_time", "is_booked"]

# View to manage time slots
def manage_time_slots(request):
    if request.method == "POST":
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            # Save the new or updated time slot to the database
            form.save()
            return redirect("manage_time_slots")  # Redirect to the same page after saving
    else:
        form = TimeSlotForm()

    # Retrieve all existing time slots from the database
    time_slots = TimeSlot.objects.all()
    services = Service.objects.all()  # Add services for dropdown in the form
    return render(request, "booking/manage_time_slots.html", {
        "form": form,
        "time_slots": time_slots,
        "services": services
    })

# API view to provide time slots data for the calendar
def time_slots_json(request):
    time_slots = TimeSlot.objects.all()
    events = []
    for slot in time_slots:
        events.append({
            "title": f"{slot.service.name} - {'Booked' if slot.is_booked else 'Available'}",
            "start": f"{slot.date}T{slot.start_time}",
            "end": f"{slot.date}T{slot.end_time}",
            "color": "#d9534f" if slot.is_booked else "#5cb85c",  # Red for booked, green for available
        })
    return JsonResponse(events, safe=False)

