from django.contrib import admin


from .models import Tablet, TabletBrandName
# Register your models here.
admin.site.register(Tablet)
admin.site.register(TabletBrandName)