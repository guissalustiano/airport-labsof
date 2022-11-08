from django.db import models
from django.urls import reverse

from flight.helper import sum_time_timedelta

class Airport(models.Model):
    name = models.CharField(max_length=256, null=False)
    code = models.CharField(max_length=32, unique=True, null=False)
    city = models.CharField(max_length=256, null=False)
    country = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'airport'

class Company(models.Model):
    name = models.CharField(max_length=256)
    website = models.URLField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'

class Flight(models.Model):
    code = models.CharField(max_length=32, unique=True, help_text='Código unico')
    departure = models.TimeField(help_text='Expected flight departure time')
    duration = models.DurationField(help_text='Expected duration')
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def arrive(self):
        return sum_time_timedelta(self.departure, self.duration)

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('flight-detail', args=[str(self.id)])

    class Meta:
        db_table = 'flight'
        ordering = ['departure']


class FlightInstance(models.Model):
    code = models.CharField(max_length=32, help_text='Code for instance, it will concat to flight')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    # https://www.flightview.com/travelTools/FTHelp/Flight_Status.htm
    STATUS = (
        ('Scheduled', 'Scheduled'), # Flight is not airborne. Departure and arrival times are according to airline's schedule.
        ('Delayed', 'Delayed'), # Flight will depart 15 or more minutes after its scheduled departure
        ('Departed', 'Departed'), # Flight has left the departure gate but may not be airborne yet.
        ('In Air', 'In Air'), # Flight is airborne. Takeoff time is actual takeoff or "wheels up" time. The arrival time is estimated. Real-time map is available.
        ('Expected', 'Expected'), # A FlightView data source indicates flight is expected to arrive at arrival airport. Usually an estimated time will be available.
        ('Diverted', 'Diverted'), # Flight has been diverted from its scheduled destination to a different location.
        ('Recovery', 'Recovery'), # Flight had departed the diverted location and enroute or landed at the scheduled destination.
        ('Landed', 'Landed'), #  Flight has landed. The landing time is actual touchdown or "wheels down."
        ('Arrived', 'Arrived'), # Flight has arrived at its destination gate.
        ('Cancelled', 'Cancelled'), # Flight has been cancelled.
        ('No Takeoff Info', 'No Takeoff Info - Call Airline'), # The real-time status of the flight is unavailable. It may have been delayed, cancelled, or the real-time status may not yet be available if the flight is international. Contact airline for more information.
        ('Past Flight', 'Past Flight'), # Flight was scheduled to operate some time in the past.
    )

    status = models.CharField(max_length=32, default='Scheduled', choices=STATUS)
    departure = models.DateTimeField(help_text='Real flight departure time')
    duration = models.DurationField(help_text='Real duration')

    def all_code(self):
       return f'{self.flight.code}-{self.code}'

    def arrive(self):
        return self.departure + self.duration

    def __str__(self):
       return self.all_code()

    def get_absolute_url(self):
        return reverse('flightinstance-detail', args=[str(self.id)])

    class Meta:
        db_table = 'flight_instance'
        ordering = ['departure']
