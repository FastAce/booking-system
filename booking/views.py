from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import Service, Booking, TimeSlot
from .forms import BookingForm, TimeSlotForm  # Import correct forms

# ---------------- HOME VIEW ---------------- #

def home(request):
    """Render the home page."""
    return render(request, "booking/home.html")


