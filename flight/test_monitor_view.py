from flight.models import FlightInstance, Airport, Company, Flight
from datetime import datetime, timedelta
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

test_username = 'testuser'
test_password = 'password'

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_superuser(test_username, f'{test_username}@mail.com', test_password)
        test_user.save()

        for airport_id in range(11):
            Airport.objects.create(
                    name=f'Airport {airport_id}',
                    code=f'C{airport_id}',
                    city='Gothan'
            )

        gru_airport = Airport.objects.create(name='Galileu', code='GLL', city='Rio Janeiro')
        cgn_airport = Airport.objects.create(name='Congonhas', code='CNG', city='São Paulo')
        company = Company.objects.create(name='Azul', website='https://www.test.com')

        for flight_id in range(15):
            flight = Flight.objects.create(
                code=f'f{flight_id}',
                departure=datetime.time(datetime.now()),
                duration=timedelta(hours=1),
                departure_airport=gru_airport,
                arrival_airport=cgn_airport,
                company=company
            )
            for instance_id in range(15):
                FlightInstance.objects.create(
                    code='i{instance_id}',
                    status='Diverted',
                    departure=datetime.now(),
                    duration=timedelta(hours=1),
                    flight=flight,
                )

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username=test_username, password=test_password)
        response = self.client.get('/airport/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username=test_username, password=test_password)
        response = self.client.get(reverse('airports'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username=test_username, password=test_password)
        response = self.client.get(reverse('airports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'flight/airport_list.html')

    def test_view_needs_auth(self):
        response = self.client.get(reverse('airports'))
        self.assertRedirects(response, '/accounts/login/?next=/airport/')

    def test_pagination_is_ten(self):
        login = self.client.login(username=test_username, password=test_password)
        response = self.client.get(reverse('airports'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['airport_list']), 10)

    def test_lists_all_authors(self):
        login = self.client.login(username=test_username, password=test_password)
        # Get second page and confirm it has (exactly) the remaining 3 items
        response = self.client.get(reverse('airports')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['airport_list']), 3)
