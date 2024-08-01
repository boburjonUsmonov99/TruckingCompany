from django.db import models


LOAD_STATUS = [
    ('dispatched', 'dispatched'),
    ('in transit', 'In Transit'),
    ('delivered', 'delivered'),
    ('cancelled', 'cancelled'),
]

class Trip(models.Model):
    # Company Information
    company_name = models.CharField(max_length=255, blank=True, null=True)
    driver_name = models.CharField(max_length=255, blank=True, null=True)
    dispatcher_name = models.CharField(max_length=255, blank=True, null=True)

    # Load Information
    broker_name = models.CharField(max_length=255, blank=True, null=True)
    load_id = models.CharField(max_length=50, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    load_status = models.CharField(max_length=50, choices=LOAD_STATUS)

    # Payment Information
    broker_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    driver_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.description

class TripLocation(models.Model):
    trip = models.ForeignKey(Trip, related_name='locations', on_delete=models.CASCADE)
    location_type = models.CharField(max_length=50, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery')])
    address = models.CharField(max_length=255)
    sequence = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ['sequence']

    def __str__(self):
        return f"{self.location_type} at {self.address} (Sequence: {self.sequence})"
