from django import forms
from .models import FuelCard, FuelCardName

class FuelCardForm(forms.ModelForm):
    class Meta:
        model = FuelCard
        fields = ['name', 'number', 'status']

class FuelCardNameForm(forms.ModelForm):
    class Meta:
        model = FuelCardName
        fields = ['name']
