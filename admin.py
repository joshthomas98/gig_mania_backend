from django.contrib import admin
from .models import Artist, Unavailability, Venue, ArtistListedGig, VenueListedGig, NewsletterSignup, MembershipOptions

admin.site.register(Artist)
admin.site.register(Unavailability)
admin.site.register(Venue)
admin.site.register(ArtistListedGig)
admin.site.register(VenueListedGig)
admin.site.register(NewsletterSignup)
admin.site.register(MembershipOptions)
