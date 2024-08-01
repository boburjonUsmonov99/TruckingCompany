from django.db import models

TABLET_ACTIVITY_STATUS = [
    ('Active', 'Active'),
    ('Inactive', 'Inactive')
]


class TabletBrandName(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the tablet brand

    def __str__(self):
        return self.name  # String representation of the tablet brand name


class SimCard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    sim_card_number = models.CharField(max_length=20, unique=True, null=True, blank=True)  # SIM card number

    def __str__(self):
        return f'{self.name} - {self.sim_card_number}'  # String representation of the SIM card


class Tablet(models.Model):
    brand = models.ForeignKey(TabletBrandName, on_delete=models.CASCADE,
                              related_name='tablets')  # Foreign key to TabletBrandName
    imei = models.CharField(max_length=250, unique=True)  # IMEI number of the tablet
    status = models.CharField(max_length=8, choices=TABLET_ACTIVITY_STATUS)  # Activity status of the tablet
    sim_card = models.ForeignKey(SimCard, on_delete=models.CASCADE, related_name='tablets')  # Foreign key to SimCard

    def __str__(self):
        return f'{self.brand.name} - {self.imei}'  # String representation of the tablet
