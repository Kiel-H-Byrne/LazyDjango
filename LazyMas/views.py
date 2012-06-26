from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Template, loader
import datetime


def splash(request):
	now = datetime.datetime.now()
	return render_to_response('countdown.html', {'current_date':now})

def home(request):
	return render_to_response('homePage.html')
	
def sandbox(request):
	cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
	]
	return render_to_response('sandBox.html', {'citys': cities} )