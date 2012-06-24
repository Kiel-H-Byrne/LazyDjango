from django.db import models

class LM_Profile(models.Model):
	fName=models.CharField(max_length=30)
	lName=models.CharField(max_length=30)
	address1=
	address2=
	city=
	state=
	zipcode=
	phone1=
	phone2=
	dob=
	e-mail=
	braSize=
	braCup=
	waist=
	hip=
	bottom=
	bottomType=
	head=
	depositAmt=
	depositPaid=
	PaymentType=
	Meal=