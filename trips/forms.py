from django import forms
from django.forms import inlineformset_factory
from .models import Trip, TripLocation

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            'company_name', 'driver_name', 'dispatcher_name', 'broker_name',
            'load_id', 'weight', 'load_status', 'broker_pay', 'driver_pay'
        ]

TripLocationFormSet = inlineformset_factory(Trip, TripLocation, fields=('location_type', 'address', 'sequence', 'date', 'time'), extra=1, can_delete=True)
