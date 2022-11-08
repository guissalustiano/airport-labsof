from collections.abc import Callable
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Airport, Flight, FlightInstance

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_flight = Flight.objects.all().count()
    num_flight_instance = FlightInstance.objects.all().count()

    context = {
        'num_flight': num_flight,
        'num_flight_instance': num_flight_instance,
    }

    return render(request, 'index.html', context=context)

# Flight
class FlightListView(generic.ListView):
    model = Flight
    paginate_by = 10

class FlightDetailView(generic.DetailView):
    model = Flight

class FlightCreate(generic.CreateView):
    model = Flight
    fields = '__all__'

class FlightUpdate(generic.CreateView):
    model = Flight
    fields = '__all__'

class FlightDelete(generic.DeleteView):
    model = Flight
    success_url = reverse_lazy('flights')

# FlightInstance
class FlightInstanceListView(generic.ListView):
    model = FlightInstance
    paginate_by = 10

class FlightInstanceDetailView(generic.DetailView):
    model = FlightInstance

class FlightInstanceCreate(generic.CreateView):
    model = FlightInstance
    fields = '__all__'

class FlightInstanceUpdate(generic.CreateView):
    model = FlightInstance
    fields = '__all__'

class FlightInstanceDelete(generic.DeleteView):
    model = FlightInstance
    success_url = reverse_lazy('flights')

# Airport
class AirportListView(generic.ListView):
    model = Airport
    paginate_by = 10

class AirportDetailView(generic.DetailView):
    model = Airport

# Report
def report_view(request):
    return render(request, 'flight/report_index.html')

def group_flights_by(f: Callable[[FlightInstance], str]):
    flights = FlightInstance.objects.all()
    groups = dict()

    for flight in flights:
        key = f(flight)

        if key not in groups:
            groups[key] = []

        groups[key].append(flight)

    return groups

def report_arrival_airport_view(request):
    context = {
        'title': 'Report by arrival airport',
        'groups': group_flights_by(lambda flight: flight.flight.arrival_airport),
    }
    return render(request, 'flight/report_list.html', context=context)

def report_departure_airport_view(request):
    context = {
        'title': 'Report by departure airport',
        'groups': group_flights_by(lambda flight: flight.flight.departure_airport),
    }
    return render(request, 'flight/report_list.html', context=context)

def report_flight_instance_status_view(request):
    context = {
        'title': 'Report by status',
        'groups': group_flights_by(lambda flight: flight.status),
    }
    return render(request, 'flight/report_list.html', context=context)
