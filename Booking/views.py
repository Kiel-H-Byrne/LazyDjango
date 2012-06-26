from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Template, loader
import datetime


def booking(request):
	return render_to_response('booking.html')
	
def bandRegister(request):
	if request.method=='POST':
		form=BandRegisterForm(request.POST)
		if form.is_valid():
		return HttpResponseRedirect('/registered/')
	else: 
		form=BandRegisterForm()
	return render(request, 'contact.html', {
		'form': form,
		})