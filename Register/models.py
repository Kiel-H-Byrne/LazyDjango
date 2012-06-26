from django.db import models

SIZE_CHOICES = (
	('XS', 'Extra Small'),
	('S', 'Small'),
	('M', 'Medium'),
	('L', 'Large'),
	('XL', 'X-Large'),
	('XXL', '2X-Large'),
)

TYPE_CHOICES = (
	('BIKINI', 'Bikini Bottom'),
	('PANT', 'Shorts'),
)

MEAL_CHOICES = (
	('VEG', 'Vegetarian'),
	('CHX', 'Non-Vegetarian'),	
)
class Profile(models.Model):
	fName=models.CharField(max_length=30)
	lName=models.CharField(max_length=30)
	slug=models.SlugField()
	address1=models.CharField(max_length=50)
	address2=models.CharField(max_length=50, null=True)
	city=models.CharField(max_length=50)
	state=models.CharField(max_length=2)
	zipcode=models.IntegerField(max_length=5)
	phone1=models.IntegerField(max_length=15)
	phone2=models.IntegerField(max_length=15, null=True)
	dob=models.DateField(blank=True, null=True)
	email=models.EmailField(max_length=50)
	braSize=models.IntegerField(max_length=2, null=True)
	braCup=models.CharField(max_length=3, null=True)
	waist=models.IntegerField(max_length=2)
	hip=models.IntegerField(max_length=2, null=True)
	bottom=models.CharField(max_length=3, choices=SIZE_CHOICES)
	bottomType=models.CharField(max_length=10, choices=TYPE_CHOICES)
	head=models.IntegerField(max_length=2, null=True)
	depositAmt=models.DecimalField(max_digits=5, decimal_places=2, null=True)
	depositPaid=models.BooleanField()
	PaymentType=models.CharField(max_length=10, null=True)
	Meal=models.CharField(max_length=10, choices=MEAL_CHOICES)
	
	def __unicode__(self):
		return self.lName