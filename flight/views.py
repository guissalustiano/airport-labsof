from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Flight, FlightInstance

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
