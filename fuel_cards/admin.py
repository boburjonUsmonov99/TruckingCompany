from django.contrib import admin


from .models import FuelCardName, FuelCard
# Register your models here.

admin.site.register(FuelCard)
admin.site.register(FuelCardName)
