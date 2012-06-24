from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Template, loader
import datetime


def booking(request):
	return render_to_response('booking.html')