from django.db import models
from django.urls import reverse

class Flight(models.Model):
    code = models.CharField(max_length=32, unique=True, help_text='Código unico')
    departure = models.TimeField(help_text='Expected flight departure time')
    duration = models.DurationField(help_text='Expected duration')

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('flight-detail', args=[str(self.id)])

    class Meta:
        ordering = ['departure']


class FlightInstance(models.Model):
    code = models.CharField(max_length=32, help_text='Code for instance, it will concat to flight')
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)

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
    departure = models.TimeField(help_text='Real flight departure time')
    duration = models.DurationField(help_text='Real duration')

    class Meta:
        ordering = ['departure']

    def __str__(self):
       return f'{self.flight.code}-{self.code}'
