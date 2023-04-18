from django.contrib import admin
from .models import Band, Availability, Venue, ArtistListedGig

admin.site.register(Band)
admin.site.register(Availability)
admin.site.register(Venue)
admin.site.register(ArtistListedGig)
