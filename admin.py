from django.contrib import admin
from .models import Artist, Unavailability, Venue, ArtistListedGig

admin.site.register(Artist)
admin.site.register(Unavailability)
admin.site.register(Venue)
admin.site.register(ArtistListedGig)
