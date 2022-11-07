from django.shortcuts import render
from django.views import generic
from .models import Flight

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_flight = Flight.objects.all().count()

    context = {
        'num_flight': num_flight
    }

    return render(request, 'index.html', context=context)

class FlightListView(generic.ListView):
    model = Flight
    paginate_by = 10

class FlightDetailView(generic.DetailView):
    model = Flight
