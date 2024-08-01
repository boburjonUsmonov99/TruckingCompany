from django.db import models

STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]

class FuelCardName(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the fuel card

    def __str__(self):
        return self.name

class FuelCard(models.Model):
    name = models.ForeignKey(FuelCardName, on_delete=models.CASCADE, related_name='fuel_card')  # Foreign key to FuelCardName
    number = models.CharField(max_length=50, unique=True)  # Number of the fuel card
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)  # Activity status of the fuel card, restricted to Active or Inactive

    def __str__(self):
        return f'{self.name} {self.number}'
