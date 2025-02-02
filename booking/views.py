from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import Service, Booking, TimeSlot
from .models import BookingForm, TimeSlotForm

# Home Page
def home(request):
    """Render the home page."""
    return render(request, "booking/home.html")

# List of available services
def services_list(request):
    """Retrieve all available services from the database."""
    services = Service.objects.all()
    return render(request, "booking/services_list.html", {"services": services})

# Form to book a service
def book_service(request):
    """Allow clients to book a service by selecting an available time slot."""
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid(): 
            booking = form.save(commit=False)

            # Marquer le créneau comme réservé
            time_slot = booking.time_slot
            if not time_slot.is_booked:
                time_slot.is_booked = True
                time_slot.save()
                booking.save()
                return HttpResponse("<h1>Reservation submitted successfully!</h1>")
            else:
                return HttpResponse("<h1>Error: Time slot already booked!</h1>")
    else:
        form = BookingForm()

    # Récupérer uniquement les créneaux disponibles
    available_time_slots = TimeSlot.objects.filter(is_booked=False)
    return render(request, "booking/book_service.html", {
        "form": form,
        "time_slots": available_time_slots
    })

# List of bookings for a user
def user_bookings(request):
    """Retrieve all bookings from the database."""
    bookings = Booking.objects.all()
    return render(request, "booking/user_bookings.html", {"bookings": bookings})

# View to manage time slots (Provider side)
def manage_time_slots(request):
    """Allow providers to manage available time slots."""
    if request.method == "POST":
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_time_slots")  # Redirect to refresh the page
    else:
        form = TimeSlotForm()

    # Retrieve all existing time slots
    time_slots = TimeSlot.objects.all()
    services = Service.objects.all()  # Add services for dropdown in the form
    return render(request, "booking/manage_time_slots.html", {
        "form": form,   
        "time_slots": time_slots,
        "services": services
    })

# API view to provide time slots data for the calendar   
def time_slots_json(request):   
    """Provide time slot data as JSON for frontend calendar display."""
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

