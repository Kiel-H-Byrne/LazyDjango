from django.forms import ModelForm
from Booking.models import Booking

class flightForm(ModelForm):
    class Meta:
        model = Flight
        exclude = ('slug', 'created',)