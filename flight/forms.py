from django import forms
from .models import Flight, FlightInstance
from datetime import datetime

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__' 


class FlightInstanceForm(forms.ModelForm):
    def clean_status(self):

        allowed_transitions = {
            'Boarding': ['Boarding', 'Scheduled', 'Canceled'],
            'Scheduled': ['Scheduled', 'Taxing', 'Canceled'],
            'Taxing': ['Taxing', 'Ready', 'Canceled'],
            'Ready': ['Ready', 'Authorized', 'Canceled'],
            'Authorized': ['Authorized', 'In flight', 'Canceled'],
            'In flight': ['In flight', 'Landed', 'Canceled'],
            'Landed': ['Landed', 'Canceled'],
            'Canceled': ['Canceled']
        }

        selected_status = self.cleaned_data['status']
        current_status = self.initial.get('status', 'Boarding')

        allowed_next_statuses = allowed_transitions.get(current_status, ['Boarding'])
        if selected_status not in allowed_next_statuses:
            raise forms.ValidationError(f'Status {selected_status} not allowed')
        return selected_status

    def clean_time(self):
        code = self.__dict__['cleaned_data']['flight']
        flight = Flight.objects.get(code=code)
        direction = flight.__dict__['direction']
        # selected_status = self.cleaned_data['status'] Não sei exatamente pq, mas agora só tem 'flight' e 'time' no cleaned_data
        selected_status = self.__dict__['data']['status']
        arriving = selected_status == 'Landed' and direction == 'A'
        departing = selected_status == 'In flight' and direction == 'D'
        if arriving or departing:
            return datetime.now()

        old_time = self.initial.get('time', datetime.now())
        return old_time

    
    class Meta:
        model = FlightInstance
        fields = '__all__'
        exclude = ('code',)

    