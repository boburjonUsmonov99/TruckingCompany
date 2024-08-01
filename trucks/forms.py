from django import forms
from .models import TruckRegistration

class TruckRegistrationForm(forms.ModelForm):
    class Meta:
        model = TruckRegistration
        fields = [
            'vin', 'license_plate_number', 'license_plate_state', 'unit_number', 'make', 'model', 'year',
            'gross_weight', 'vehicle_type', 'registration_expiration', 'fuel_type', 'axle_count',
            'usdot_number', 'registrant_name', 'registrant_address1', 'registrant_address2',
            'registrant_city', 'registrant_state', 'registrant_zip'
        ]
