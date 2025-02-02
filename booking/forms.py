from django import forms
from .models import Booking, Service, TimeSlot

# Booking form (Client)
class BookingForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Services"
    )
    
    time_slot = forms.ModelChoiceField(
        queryset=TimeSlot.objects.filter(is_booked=False),
        empty_label="Select an available time slot",
        label="Available Time Slots"
    )

    class Meta:
        model = Booking
        fields = ['client_name', 'client_email', 'services', 'time_slot']

# Time Slot Management Form (Provider)
class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['provider', 'service', 'date', 'start_time', 'end_time', 'is_booked']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }

