from django.db import models

BAND_CHOICES = (
	('YUMA', 'Yuma'),
)

SECTION_CHOICES = (
	('GODS_OF_WAR', 'Gods of War'),
	('ANGRY_BIRDS', 'Angry Birds'),	
)

class Flight(models.Model):
	name=models.CharField(max_length=20)
	flightNum=models.CharField(max_length=10)
	slug=models.SlugField()
	departDate=models.DateTimeField()
	arriveDate=models.DateTimeField()
	departAirport=models.DateTimeField()
	arriveAirport=models.DateTimeField()
	resNum=models.CharField(max_length=50)
	cost=models.DecimalField(decimal_places=2, max_digits=6)

	def __unicode__(self):
		return self.name

class MasSection(models.Model):
	name=models.CharField(max_length=20, choices=SECTION_CHOICES)
	slug=models.SlugField(max_length=50)
	theme=models.TextField()
	image=models.ImageField(upload_to='Booking/Sections')

	def __unicode__(self):
		return self.name

class MasBand(models.Model):	
	name=models.CharField(max_length=20, choices=BAND_CHOICES)
	slug=models.SlugField()
	theme=models.TextField()
	sections=models.ManyToManyField(MasSection)
	image=models.ImageField(upload_to='Booking/Bands', blank=True)

	def __unicode__(self):
		return self.name

class MasPackage(models.Model):
	name=models.CharField(max_length=30)
	slug=models.SlugField()
	band=models.ForeignKey(MasBand)
	section=models.ForeignKey(MasSection)
	images=models.ImageField(upload_to='Booking/Costumes')
	cost=models.DecimalField(decimal_places=2, max_digits=6)

	def __unicode__(self):
		return self.name

class JouvertSection(models.Model):
	name=models.CharField(max_length=20)
	slug=models.SlugField(max_length=50)
	theme=models.TextField()
	image=models.ImageField(upload_to='Booking/Sections')

	def __unicode__(self):
		return self.name

class JouvertBand(models.Model):	
	name=models.CharField(max_length=20)
	slug=models.SlugField()
	theme=models.TextField()
	sections=models.ManyToManyField(JouvertSection)
	image=models.ImageField(upload_to='Booking/Bands', blank=True)

	def __unicode__(self):
		return self.name

class JouvertPackage(models.Model):
	name=models.CharField(max_length=30)
	slug=models.SlugField()
	band=models.ForeignKey(JouvertBand)
	section=models.ForeignKey(MasSection)
	images=models.ImageField(upload_to='Booking/Costumes')
	cost=models.DecimalField(decimal_places=2, max_digits=6)

	def __unicode__(self):
		return self.name 
	
class Lodging(models.Model):
	name=models.CharField(max_length=30)
	slug=models.SlugField()
	type=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	distance=models.IntegerField()
	image=models.ImageField(upload_to='Booking/Lodgings')
	rooms=models.IntegerField()
	cost=models.DecimalField(decimal_places=2, max_digits=6)

	def __unicode__(self):
		return self.name

class Fete(models.Model):
	name=models.CharField(max_length=30)
	slug=models.SlugField()
	type=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	dressCode=models.CharField(max_length=30)
	cost=models.DecimalField(decimal_places=2, max_digits=6)
	image=models.ImageField(upload_to='Booking/Fetes')
	byob=models.BooleanField()
	inclusive=models.BooleanField()

	def __unicode__(self):
		return self.name
