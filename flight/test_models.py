from django.test import TestCase
from datetime import datetime, timedelta

from flight.models import (
    Airport, 
    Company, 
    FlightInstance, Flight
)

class CompanyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name='Azul', website='https://www.test.com')

    def test_generate_id(self):
        company = Company.objects.get(name='Azul')
        self.assertEqual(company.id, 1)

    def test_update(self):
        company = Company.objects.get(name='Azul')
        company.name = 'Vermelho'
        company.save()
        self.assertEquals(company.name, 'Vermelho')

    def test_delete(self):
        company = Company.objects.get(name='Azul')
        company.delete()
        self.assertEqual(Company.objects.count(), 0)

class AirportModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Airport.objects.create(name='Guarulhos', code='GRU', city='São Paulo')

    def test_generate_id(self):
        airport = Airport.objects.get(code='GRU')
        self.assertEqual(airport.id, 1)

    def test_update(self):
        airport = Airport.objects.get(code='GRU')
        airport.name = 'Guarulhoz'
        airport.save()
        self.assertEquals(airport.name, 'Guarulhoz')

    def test_delete(self):
        airport = Airport.objects.get(code='GRU')
        airport.delete()
        self.assertEqual(Airport.objects.count(), 0)

class FlightModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        airport1 = Airport.objects.create(name='Airport 1', code='AP1', city='São Paulo')
        airport2 = Airport.objects.create(name='Airport 2', code='AP2', city='São Paulo')
        company = Company.objects.create(name='Company', website='https://www.test.com')

        flight = Flight.objects.create(
            code='L512',
            departure=datetime.time(datetime.now()),
            duration=timedelta(hours=1),
            departure_airport=airport1,
            arrival_airport=airport2,
            company=company
        )

        FlightInstance.objects.create(
            code='L512-01',
            status='Embarque',
            departure=datetime.now(),
            arrival=datetime.now(),
            flight=flight,
        )

    def test_generate_id(self):
        airport = FlightInstance.objects.get(code='L512-01')
        self.assertEqual(airport.id, 1)

    def test_update(self):
        airport = FlightInstance.objects.get(code='L512-01')
        airport.status = 'Em Voo'
        airport.save()
        self.assertEquals(airport.status, 'Em Voo')

    def test_delete(self):
        airport = FlightInstance.objects.get(code='L512-01')
        airport.delete()
        self.assertEqual(FlightInstance.objects.count(), 0)

class FlightModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        gru_airport = Airport.objects.create(name='Galileu', code='GLL', city='Rio Janeiro')
        cgn_airport = Airport.objects.create(name='Congonhas', code='CNG', city='São Paulo')
        company = Company.objects.create(name='Azul', website='https://www.test.com')

        Flight.objects.create(
            code='L512',
            departure=datetime.time(datetime.now()),
            duration=timedelta(hours=1),
            departure_airport=gru_airport,
            arrival_airport=cgn_airport,
            company=company
        )

    def test_generate_id(self):
        flight = Flight.objects.get(code='L512')
        self.assertEqual(flight.id, 1)

    def test_update(self):
        flight = Flight.objects.get(code='L512')
        flight.duration = timedelta(hours=2)
        flight.save()
        self.assertEquals(flight.duration, timedelta(hours=2))

    def test_delete(self):
        route = Flight.objects.get(code='L512')
        route.delete()
        self.assertEqual(Flight.objects.count(), 0)
