from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

from flight.helper import sum_time_timedelta


class Airport(models.Model):
    name = models.CharField(max_length=256, null=False)
    code = models.CharField(max_length=32, unique=True, null=False)
    city = models.CharField(max_length=256, null=False)
    country = models.CharField(max_length=256, null=False)
    # arrival (Generate by Flight)
    # departure (Generate by Flight)

    def instances(self):
        return [inst for flight in self.flight.all() for inst in flight.instance.all()]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('airport-detail', args=[str(self.id)])

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
    validate_code = RegexValidator(
        '^[A-Z]{3}[0-9]+$', 'Code must be in the format ABC1234')
    code = models.CharField(max_length=32, unique=True,
                            help_text='Unique code, 3 letters followed by numbers', validators=[validate_code])
    direction = models.CharField(max_length=10, choices=[(
        'Arrival', 'Arrival'), ('Departure', 'Departure')], default='Departure')
    time = models.TimeField(
        help_text='Expected time for departure or arrival, in HH:MM format')
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def arrive(self):
        return self.time

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('flight-detail', args=[str(self.id)])

    def get_direction(self):
        return self.direction

    class Meta:
        db_table = 'flight'
        ordering = ['time']


class FlightInstance(models.Model):
    validate_code = RegexValidator(
        '^[0-9]+$', 'Code must be in the format 1234')
    code = models.CharField(max_length=32, unique=True,
                            help_text="Code for instance, it will concat to flight's code, numbers only", validators=[validate_code])
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name='instance')

    STATUS = (
        ('Boarding', 'Boarding'),  # Embarcando
        ('Scheduled', 'Scheduled'),  # Programado
        ('Taxing', 'Taxing'),  # Taxiando
        ('Ready', 'Ready'),  # Pronto
        ('Authorized', 'Authorized'),  # Autorizado
        ('In flight', 'In flight'),  # Em voo
        ('Landed', 'Landed'),  # Aterrissado
        ('Canceled', 'Canceled'),  # Cancelado
    )

    status = models.CharField(
        max_length=32, choices=STATUS, default='Boarding')
    time = models.DateTimeField(
        help_text="Real time for departure or arrival, in YYYY-MM-DD HH:MM format")

    def all_code(self):
        return f'{self.flight.code}-{self.code}'

    def __str__(self):
        return self.all_code()

    def get_absolute_url(self):
        return reverse('flightinstance-detail', args=[str(self.id)])

    class Meta:
        db_table = 'flight_instance'
        ordering = ['time']
        permissions = (
            ('can_list_report', 'List report'),
            ('can_arrive_report', 'Arrive airport report'),
            ('can_departure_report', 'Departure airport report'),
            ('can_status_report', 'Flight Status report'),
        )
