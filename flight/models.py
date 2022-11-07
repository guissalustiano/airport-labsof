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
        ('Scheduled', 'Scheduled'),
        ('Delayed', 'Delayed'),
        ('Departed', 'Departed'),
        ('In Air', 'In Air'),
        ('Expected', 'Expected'),
        ('Diverted', 'Diverted'),
        ('Recovery', 'Recovery'),
        ('Landed', 'Landed'),
        ('Arrived', 'Arrived'),
        ('Cancelled', 'Cancelled'),
        ('No Takeoff Info', 'No Takeoff Info - Call Airline'),
        ('Past Flight', 'Past Flight'),
    )

    status = models.CharField(max_length=32, default='Scheduled', choices=STATUS)
    departure = models.TimeField(help_text='Real flight departure time')
    duration = models.DurationField(help_text='Real duration')

    class Meta:
        ordering = ['departure']

    def __str__(self):
       return f'{self.flight.code}-{self.code}'
