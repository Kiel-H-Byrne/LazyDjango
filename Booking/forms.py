from django import forms
from django.forms import ModelForm
from Booking import models


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        exclude = ('slug', )
        
class MasSectionForm(ModelForm):
    class Meta:
        model = MasSection
        exclude = ('slug', )

class MasBandForm(ModelForm):	
    class Meta:
        model = MasBand
        exclude = ('slug', )

class MasPackageForm(ModelForm):
    class Meta:
        model = MasPackage
        exclude = ('slug', )

class JouvertSectionForm(ModelForm):
    class Meta:
        model = JouvertSection
        exclude = ('slug', )

class JouvertBandForm(ModelForm):	
    class Meta:
        model = JouvertBand
        exclude = ('slug', )

class JouvertPackageForm(ModelForm):
    class Meta:
        model = JouvertPackage
        exclude = ('slug', )
	
class LodgingForm(ModelForm):
    class Meta:
        model = Lodging
        exclude = ('slug', )

class FeteForm(ModelForm):
    class Meta:
        model = Fete
        exclude = ('slug', )
