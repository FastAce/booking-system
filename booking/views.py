from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import Service, Booking, TimeSlot
from .forms import BookingForm, TimeSlotForm  # Import correct des forms

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

            # Vérifier si le créneau est toujours disponible
            time_slot = booking.time_slot
            if not time_slot.is_booked:
                time_slot.is_booked = True
                time_slot.save()
                
                booking.date = time_slot.date
                booking.time = time_slot.start_time
                booking.save()

                # Ajouter plusieurs services à la réservation
                form.save_m2m()

                return redirect("user_bookings")  # Redirige vers la liste des réservations
            else:
                return HttpResponse("<h1>Error: Time slot already booked!</h1>")
    else:
        form = BookingForm()

    available_time_slots = TimeSlot.objects.filter(is_booked=False)
    services = Service.objects.all()  # Ajout des services
    return render(request, "booking/book_service.html", {
        "form": form,
        "time_slots": available_time_slots,
        "services": services
    })

# List of bookings for a user
def user_bookings(request):
    """Retrieve all bookings from the database and improve display."""
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

