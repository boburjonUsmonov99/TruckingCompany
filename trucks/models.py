from django.db import models

AMERICAN_STATES = [
    ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"), ("CA", "California"),
    ("CO", "Colorado"), ("CT", "Connecticut"), ("DE", "Delaware"), ("FL", "Florida"), ("GA", "Georgia"),
    ("HI", "Hawaii"), ("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"),
    ("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"), ("MD", "Maryland"),
    ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"), ("MS", "Mississippi"),
    ("MO", "Missouri"), ("MT", "Montana"), ("NE", "Nebraska"), ("NV", "Nevada"), ("NH", "New Hampshire"),
    ("NJ", "New Jersey"), ("NM", "New Mexico"), ("NY", "New York"), ("NC", "North Carolina"),
    ("ND", "North Dakota"), ("OH", "Ohio"), ("OK", "Oklahoma"), ("OR", "Oregon"), ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"), ("SC", "South Carolina"), ("SD", "South Dakota"), ("TN", "Tennessee"),
    ("TX", "Texas"), ("UT", "Utah"), ("VT", "Vermont"), ("VA", "Virginia"), ("WA", "Washington"),
    ("WV", "West Virginia"), ("WI", "Wisconsin"), ("WY", "Wyoming"),
]

FUEL_TYPES = [
    ('Diesel', 'Diesel'),
    ('Electricity', 'Electricity'),
]
class TruckRegistration(models.Model):
    vin = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number
    license_plate_number = models.CharField(max_length=10, unique=True)  # License Plate Number
    license_plate_state = models.CharField(max_length=2, choices=AMERICAN_STATES)  # License Plate State
    unit_number = models.CharField(max_length=50)  # Unit Number of the truck
    make = models.CharField(max_length=50)  # Vehicle Make
    model = models.CharField(max_length=50)  # Vehicle Model
    year = models.PositiveIntegerField()  # Vehicle Year
    gross_weight = models.FloatField()  # Combined Gross Weight of the vehicle
    vehicle_type = models.CharField(max_length=50)  # Type of the vehicle
    registration_expiration = models.DateField()  # Registration Expiration Date
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPES)  # Fuel Type of the vehicle, restricted to Diesel or Electricity
    axle_count = models.PositiveIntegerField()  # Axle Count of the vehicle

    usdot_number = models.CharField(max_length=20)  # USDOT Number of the registrant
    registrant_name = models.CharField(max_length=100)  # Name of the registrant
    registrant_address1 = models.CharField(max_length=255)  # Address Line 1 of the registrant
    registrant_address2 = models.CharField(max_length=255, blank=True, null=True)  # Address Line 2 of the registrant (optional)
    registrant_city = models.CharField(max_length=100)  # City of the registrant's address
    registrant_state = models.CharField(max_length=2, choices=AMERICAN_STATES)  # State of the registrant's address
    registrant_zip = models.CharField(max_length=20)  # ZIP Code of the registrant's address

    def __str__(self):
        return f'{self.vin} - {self.license_plate_number}'  # String representation of the truck




