from django.shortcuts import render, redirect
from .forms import BookingForm

def book_service(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("services_list")  # Redirige après la réservation
    else:
        form = BookingForm()
    return render(request, "booking/book_service.html", {"form": form})

