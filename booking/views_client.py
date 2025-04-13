from django.shortcuts import render, redirect
from .models import Service, Booking, TimeSlot
from .forms import BookingForm

# Client - Book a service
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

                return redirect("client:user_bookings")  # Redirect to client bookings page
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

# Client - View bookings
def user_bookings(request):
    """Retrieve all bookings for a user."""
    bookings = Booking.objects.all()
    return render(request, "client/user_bookings.html", {"bookings": bookings})

