from django.contrib import admin
from .models import Trip, TripLocation

class TripLocationInline(admin.TabularInline):
    model = TripLocation
    extra = 1

class TripAdmin(admin.ModelAdmin):
    list_display = (
        'company_name', 'driver_name', 'dispatcher_name', 'broker_name',
        'load_id', 'weight', 'load_status', 'broker_pay', 'driver_pay'
    )
    inlines = [TripLocationInline]

admin.site.register(Trip, TripAdmin)
admin.site.register(TripLocation)
