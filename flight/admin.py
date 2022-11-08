from django.contrib import admin
from .models import Airport, Company, Flight, FlightInstance

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    pass

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    pass

@admin.register(FlightInstance)
class FlightInstanceAdmin(admin.ModelAdmin):
    pass
