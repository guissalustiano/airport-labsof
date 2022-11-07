from django.contrib import admin
from .models import Flight, FlightInstance

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    pass

@admin.register(FlightInstance)
class FlightInstanceAdmin(admin.ModelAdmin):
    pass
