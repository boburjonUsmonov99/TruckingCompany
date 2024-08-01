from django.db import models

STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]

class TransponderNameList(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the transponder

    def __str__(self):
        return self.name

class Transponder(models.Model):
    name = models.ForeignKey(TransponderNameList, on_delete=models.CASCADE, related_name='transponder')  # Foreign key to TransponderName
    number = models.CharField(max_length=50, unique=True)  # Number of the transponder
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)  # Activity status of the transponder, restricted to Active or Inactive

    def __str__(self):
        return f'{self.name} {self.number}'
