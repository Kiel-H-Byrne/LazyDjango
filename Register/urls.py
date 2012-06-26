from django.conf.urls import patterns, include, url

urlpatterns = patterns('Register.views',
#	url(r'^$', 'register', name='register'),
	url(r'^$', 'manage_profile', name='manage_profile'),	
	)