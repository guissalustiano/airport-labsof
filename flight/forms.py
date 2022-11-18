from django import forms
from .models import Flight, FlightInstance

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__' 


class FlightInstanceForm(forms.ModelForm):
    def clean_status(self):

        allowed_transitions = {
            'Scheduled': ['Scheduled', 'Onboarding', 'Cancelled'],
            'Onboarding': ['Onboarding', 'Taxing', 'Cancelled'],
            'Taxing': ['Taxing', 'Departed', 'Cancelled'],
            'Departed': ['Departed', 'Arrived', 'Cancelled'],
            'Arrived': ['Arrived'],
            'Cancelled': ['Cancelled']
        }


        # objects = Flight.objects.all()
        # print(self)
        # print(self.__dict__)
        # print(objects[0][])
        # pega current_status a partir do objects
        # current_status = 'Scheduled'

        current_status = self.initial.get('status', 'Scheduled')
        selected_status = self.cleaned_data['status']

        allowed_next_statuses = allowed_transitions.get(current_status, ['Scheduled'])
        if selected_status not in allowed_next_statuses:
            raise forms.ValidationError(f'Status {selected_status} not allowed')
        return selected_status
    
    class Meta:
        model = FlightInstance
        fields = '__all__'
        exclude = ('code', )

    