from django.conf.urls import patterns, include, url

urlpatterns = patterns('Booking.views',
	url(r'^$', 'booking', name='booking'),
#    url(r'^flights/$', 'flights', name='flights'),
#    url(r'^rooms/$', 'rooms', name='rooms'),
#    url(r'^costumes/$', 'costumes', name='costumes'),
#    url(r'^fetes/$', 'fetes', name='fetes'),
#    url(r'^packages/$', 'packages', name='packages'),
)