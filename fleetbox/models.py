from django.db import models

# Create your models here.



class Fleetbox(models.Model):
    fleet_box_id = models.AutoField(primary_key=True)  # Define your custom primary key field

    # FOREIGN KEYS:
    #Drivers:
    assigned_driver = models.ForeignKey('drivers.Driver', on_delete=models.CASCADE, related_name='drivers_assigned', null=True, blank=True)
    assigned_driver_co_driver = models.ForeignKey('drivers.Driver', on_delete=models.CASCADE, related_name='drivers_assigned_co_driver', null=True, blank=True)

    # Trucks
    assigned_truck = models.ForeignKey('trucks.TruckRegistration', to_field='vin', on_delete=models.CASCADE, related_name='drivers_assigned_vin', null=True, blank=True)

    # Transponders
    assigned_transponder = models.ForeignKey('transponders.Transponder', to_field='number', on_delete=models.CASCADE, related_name='drivers_assigned_transponder_number', null=True, blank=True)

    # Fuel Cards
    assigned_fuel_card = models.ForeignKey('fuel_cards.FuelCard', to_field='number', on_delete=models.CASCADE, related_name='drivers_assigned_fuel_card_number', null=True, blank=True)

    # Tablets
    assigned_tablet_imei = models.ForeignKey('tablets.Tablet', to_field='imei', on_delete=models.CASCADE, related_name='drivers_assigned_tablet_sim', null=True, blank=True)

    def __str__(self):
        return f'{self.fleet_box_id} - {self.assigned_driver} - {self.assigned_truck}'  # String representation of the truck
