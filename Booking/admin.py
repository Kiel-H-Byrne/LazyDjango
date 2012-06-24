from django.contrib import admin
#from django.template.defaultfilters import slugify

from Booking.models import Flight, MasSection, MasBand, MasPackage, JouvertSection, JouvertBand, JouvertPackage, Lodging, Fete


class FlightAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class MasBandAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class MasSectionAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class MasPackageAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class JouvertBandAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class JouvertSectionAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class JouvertPackageAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}	

class LodgingAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class FeteAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

admin.site.register(Flight, FlightAdmin)
admin.site.register(MasBand, MasBandAdmin)
admin.site.register(MasSection, MasSectionAdmin)
admin.site.register(MasPackage, MasPackageAdmin)
admin.site.register(JouvertBand, JouvertBandAdmin)
admin.site.register(JouvertSection, JouvertSectionAdmin)
admin.site.register(JouvertPackage, JouvertPackageAdmin)
admin.site.register(Lodging, LodgingAdmin)
admin.site.register(Fete, FeteAdmin)

