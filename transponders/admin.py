from django.contrib import admin

from .models import Transponder, TransponderNameList
# Register your models here.

admin.site.register(Transponder)
admin.site.register(TransponderNameList)