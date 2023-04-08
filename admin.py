from django.contrib import admin
from .models import Band, Venue, ArtistListedGig

admin.site.register(Band)
admin.site.register(Venue)
admin.site.register(ArtistListedGig)
