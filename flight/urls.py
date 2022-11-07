from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flight/', views.FlightListView.as_view(), name='flights'),
    path('flight/<int:pk>', views.FlightDetailView.as_view(), name='flight-detail'),
]
