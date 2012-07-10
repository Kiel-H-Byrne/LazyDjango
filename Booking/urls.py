from django.conf.urls import patterns, include, url

urlpatterns = patterns('Booking',
	url(r'^$', 'views.booking', name='booking'),
    url(r'^flights/$', 'flights.flights', name='flights'),
    url(r'^rooms/$', 'rooms', name='rooms'),
    url(r'^costumes/$', 'costumes', name='costumes'),
    url(r'^fetes/$', 'fetes', name='fetes'),
    url(r'^packages/$', 'packages', name='packages'),
)