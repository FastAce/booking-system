from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Service, TimeSlot
from .forms import TimeSlotForm

# Provider - Manage time slots
def manage_time_slots(request):
    """Allow providers to manage available time slots."""
    if request.method == "POST":
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("provider:manage_time_slots")  # Refresh the page
    else:
        form = TimeSlotForm()

    time_slots = TimeSlot.objects.all()
    services = Service.objects.all()  # Retrieve all services for the provider
    return render(request, "provider/manage_time_slots.html", {
        "form": form,
        "time_slots": time_slots,
        "services": services
    })

# Provider - View services list
def services_list(request):
    """Retrieve all available services for the provider."""
    services = Service.objects.all()
    return render(request, "provider/services_list.html", {"services": services})

# Provider - API to provide time slots data for calendar
def time_slots_json(request):
    """Provide time slot data as JSON for frontend calendar display."""
    time_slots = TimeSlot.objects.all()
    events = []
    for slot in time_slots:
        events.append({
            "title": f"{slot.service.name} - {'Booked' if slot.is_booked else 'Available'}",
            "start": f"{slot.date}T{slot.start_time}",
            "end": f"{slot.date}T{slot.end_time}",
            "color": "#d9534f" if slot.is_booked else "#5cb85c",
        })
    return JsonResponse(events, safe=False)
