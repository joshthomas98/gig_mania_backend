from django.contrib import admin
from .models import Artist, Availability, Venue, ArtistListedGig

admin.site.register(Artist)
admin.site.register(Availability)
admin.site.register(Venue)
admin.site.register(ArtistListedGig)
