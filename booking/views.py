from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import Service, Booking, TimeSlot
from .forms import BookingForm, TimeSlotForm  # Import correct forms

# ---------------- HOME VIEW ---------------- #

def home(request):
    """Render the home page."""
    return render(request, "booking/home.html")


# ---------------- CLIENT VIEWS ---------------- #

def book_service(request):
    """Allow clients to book a service by selecting an available time slot."""
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid(): 
            booking = form.save(commit=False)

            # Check if the selected time slot is still available
            time_slot = booking.time_slot
            if not time_slot.is_booked:
                time_slot.is_booked = True
                time_slot.save()
                
                booking.date = time_slot.date
                booking.time = time_slot.start_time
                booking.save()

                # Save multiple services in the booking
                form.save_m2m()

                return redirect("user_bookings")  # Redirect to client bookings page
            else:
                return HttpResponse("<h1>Error: Time slot already booked!</h1>")
    else:
        form = BookingForm()

    available_time_slots = TimeSlot.objects.filter(is_booked=False)
    services = Service.objects.all()  # Retrieve all available services
    return render(request, "client/book_service.html", {
        "form": form,
        "time_slots": available_time_slots,
        "services": services
    })

def user_bookings(request):
    """Retrieve all bookings for a user."""
    bookings = Booking.objects.all()
    return render(request, "client/user_bookings.html", {"bookings": bookings})


# ---------------- PROVIDER VIEWS ---------------- #

def manage_time_slots(request):
    """Allow providers to manage available time slots."""
    if request.method == "POST":
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_time_slots")  # Refresh the page
    else:
        form = TimeSlotForm()

    time_slots = TimeSlot.objects.all()
    services = Service.objects.all()  # Retrieve all services for the provider
    return render(request, "provider/manage_time_slots.html", {
        "form": form,
        "time_slots": time_slots,
        "services": services
    })

def services_list(request):
    """Retrieve all available services for the provider."""
    services = Service.objects.all()
    return render(request, "provider/services_list.html", {"services": services})


# ---------------- API FOR TIME SLOTS (Calendar) ---------------- #

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

