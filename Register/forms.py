from django import forms
from django.forms import ModelForm
from Register import models

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('slug',)