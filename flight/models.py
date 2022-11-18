from django.db import models
from django.urls import reverse

from flight.helper import sum_time_timedelta

class Airport(models.Model):
    name = models.CharField(max_length=256, null=False)
    code = models.CharField(max_length=32, unique=True, null=False)
    city = models.CharField(max_length=256, null=False)
    country = models.CharField(max_length=256, null=False)
    # arrival (Generate by Flight)
    # departure (Generate by Flight)

    def departure_instances(self):
        return [inst for flight in self.departure.all() for inst in flight.instance.all()]

    def arrival_instances(self):
        return [inst for flight in self.arrival.all() for inst in flight.instance.all()]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('airport-detail', args=[str(self.id)])

    class Meta:
        db_table = 'airport'
        permissions = (
            ('can_list', 'List airport (monitor)'),
            ('can_detail', 'Detail airport (monitor)'),
        )

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
        permissions = (
            ('can_create', 'Create flight'),
            ('can_update', 'Update flight'),
            ('can_delete', 'Delete flight'),
            ('can_list', 'List flight'),
            ('can_detail', 'Detail flight'),
        )


class FlightInstance(models.Model):
    code = models.CharField(max_length=32, help_text='Code for instance, it will concat to flight')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='instance')

    # https://www.flightview.com/travelTools/FTHelp/Flight_Status.htm
    STATUS = (
        ('Scheduled', 'Scheduled'), # Flight is not airborne. Departure and arrival times are according to airline's schedule.
        ('Onboarding', 'Onboarding'), # 
        ('Taxing', 'Taxing'), # Airplane has left the gate and is awaiting permission to fly
        ('Departed', 'Departed'), # Flight has left the airport.
        ('Arrived', 'Arrived'), # Flight has arrived at its destination gate.
        ('Cancelled', 'Cancelled'), # Flight has been cancelled.
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
        permissions = (
            ('can_create', 'Create flightinstance'),
            ('can_update', 'Update flightinstance'),
            ('can_delete', 'Delete flightinstance'),
            ('can_list', 'List flightinstance'),
            ('can_detail', 'Detail flightinstance'),

            ('can_report_list', 'List report'),
            ('can_report_arrive', 'Arrive airport report'),
            ('can_report_departure', 'Departure airport report'),
            ('can_report_statue', 'Flight Status report'),
        )
