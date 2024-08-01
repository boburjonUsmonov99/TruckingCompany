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

TRUCK_STATUS_CHOICES = [('Owner Operator', 'Owner Operator'),
                        ('Company Driver', 'Company Driver'),
                        ('Lease Operator', 'Lease Operator')]

EMPLOYMENT_STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive'),]

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'),]

PAYMENT_TYPE_CHOICES = [('Percentage', 'Percentage'),
                        ('Pay Per Mile', 'Pay Per Mile'),
                        ('Flat Pay', 'Flat Pay'),
                        ('Hourly Pay', 'Hourly Pay')]

class Driver(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=AMERICAN_STATES)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    license_number = models.CharField(max_length=50, unique=True)
    license_state = models.CharField(max_length=2, choices=AMERICAN_STATES)
    license_expiration = models.DateField()
    experience_months = models.PositiveIntegerField()
    experience_years = models.PositiveIntegerField()
    hire_date = models.DateField()
    employment_status = models.CharField(max_length=8, choices=EMPLOYMENT_STATUS_CHOICES)
    truck_status = models.CharField(max_length=20, choices=TRUCK_STATUS_CHOICES)

    # Contract
    payment_type = models.CharField(max_length=12, choices=PAYMENT_TYPE_CHOICES)
    percentage = models.FloatField(null=True, blank=True)
    loaded_mile_rate = models.FloatField(null=True, blank=True)
    empty_mile_rate = models.FloatField(null=True, blank=True)
    flat_amount = models.FloatField(null=True, blank=True)
    days_week = models.PositiveIntegerField(null=True, blank=True)
    hourly_payment = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
