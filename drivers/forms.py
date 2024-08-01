from django import forms
from .models import Driver

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            'first_name', 'last_name', 'phone_number', 'email', 'gender',
            'address_line1', 'address_line2', 'city', 'state', 'country',
            'zip_code', 'date_of_birth', 'license_number', 'license_state',
            'license_expiration', 'experience_months', 'experience_years',
            'hire_date', 'employment_status', 'truck_status', 'payment_type',
            'percentage', 'loaded_mile_rate', 'empty_mile_rate', 'flat_amount',
            'days_week', 'hourly_payment'
        ]

class DriverCreateForm(DriverForm):
    pass  # Add custom validation or fields if needed

class DriverRetrieveForm(DriverForm):
    pass  # Add custom logic if needed

class DriverUpdateForm(DriverForm):
    pass  # Add custom validation or fields if needed

class DriverDeleteForm(DriverForm):
    pass  # Add custom logic if needed
