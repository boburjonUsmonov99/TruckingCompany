from django import forms
from .models import Transponder, TransponderNameList

class TransponderForm(forms.ModelForm):
    class Meta:
        model = Transponder
        fields = ['name', 'number', 'status']

class TransponderNameForm(forms.ModelForm):
    class Meta:
        model = TransponderNameList
        fields = ['name']
