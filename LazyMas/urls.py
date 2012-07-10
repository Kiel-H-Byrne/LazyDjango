from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('LazyMas.views',
	url(r'^$', 'splash'),
	url(r'^index\.[a-t]+$', 'splash', name='splash'),

	url(r'^home/$', 'home', name='home'),
#ADMIN
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),	
    
	url(r'^sand/$', 'sandbox', name='sandbox', ),
)

urlpatterns += patterns('LazyMas.views',
#APPS
    url(r'^register/', include('Register.urls')),
#    url(r'^login/', include('Login.urls')),
#    url(r'^dashboard/', include('Dashboard.urls')),
    url(r'^booking/', include('Booking.urls')),
#    url(r'^faq/', include('FAQ.urls')),
#    url(r'^contact/', include('Contact.urls')),
#    url(r'^swag/', include('Swag.urls')),
#    url(r'^blog/', include('Blog.urls')),
)

urlpatterns += staticfiles_urlpatterns()


