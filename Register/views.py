from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Template, loader
import datetime
from django.forms.models import modelformset_factory
from Register import models

def register(request):
	if request.method=='POST':
		form = ProfileForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/registered/')
		else: 
			form=RegisterForm()
		return render_to_response('Register/LMregister.html', {'form':form,},)
	else:
		return HttpResponse('Sorry, No data submitted',)

def manage_profile(request):
    ProfileFormSet = modelformset_factory(models.Profile)
    if request.method == 'POST':
        formset = ProfileFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = ProfileFormSet()
    return render_to_response("register/manage_profile.html", {
        "formset": formset,
    })