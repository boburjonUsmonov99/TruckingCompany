from django import forms
from .models import Tablet, TabletBrandName, SimCard

class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        fields = ['brand', 'imei', 'status', 'sim_card']

class TabletBrandNameForm(forms.ModelForm):
    class Meta:
        model = TabletBrandName
        fields = ['name']

class SimCardForm(forms.ModelForm):
    class Meta:
        model = SimCard
        fields = ['name', 'sim_card_number']
