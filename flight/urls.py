from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flight/', views.FlightListView.as_view(), name='flights'),
    path('flight/<int:pk>', views.FlightDetailView.as_view(), name='flight-detail'),
    path('flight/create/', views.FlightCreate.as_view(), name='flight-create'),
    path('flight/<int:pk>/update/', views.FlightUpdate.as_view(), name='flight-update'),
    path('flight/<int:pk>/delete/', views.FlightDelete.as_view(), name='flight-delete'),
    path('flight-instance/', views.FlightInstanceListView.as_view(), name='flightinstances'),
    path('flight-instance/<int:pk>', views.FlightInstanceDetailView.as_view(), name='flightinstance-detail'),
    path('flight-instance/create/', views.FlightInstanceCreate.as_view(), name='flightinstance-create'),
    path('flight-instance/<int:pk>/update/', views.FlightInstanceUpdate.as_view(), name='flightinstance-update'),
    path('flight-instance/<int:pk>/delete/', views.FlightInstanceDelete.as_view(), name='flightinstance-delete'),
    path('airport/', views.AirportListView.as_view(), name='airports'),
    path('airport/<int:pk>', views.AirportDetailView.as_view(), name='airport-detail'),
    path('report/', views.report_view, name='reports'),
    path('report/arrival-airport', views.report_arrival_airport_view, name='report-arrival-airport'),
    path('report/departure-airport', views.report_departure_airport_view, name='report-departure-airpot'),
    path('report/flight-instance-status', views.report_flight_instance_status_view, name='report-flight-instance-status'),
]
