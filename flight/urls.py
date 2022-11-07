from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flight/', views.FlightListView.as_view(), name='flights'),
    path('flight/<int:pk>', views.FlightDetailView.as_view(), name='flight-detail'),
    path('flight/create/', views.FlightCreate.as_view(), name='flight-create'),
    path('flight/<int:pk>/update/', views.FlightUpdate.as_view(), name='flight-update'),
    path('flight/<int:pk>/delete/', views.FlightDelete.as_view(), name='flight-delete'),
]
