from rest_framework import serializers
from .models import Band, Availability, Venue, ArtistListedGig


class BandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Band
        fields = ['id', 'band_name', 'email', 'username',
                  'password', 'genre', 'country', 'county']


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = ['id', 'band', 'date']


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ['id', 'venue_name', 'email', 'username',
                  'password', 'type_of_music']


class ArtistListedGigSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtistListedGig
        fields = ['id', 'artist_name', 'date_of_gig', 'country_of_venue', 'venue_name',
                  'genre_of_gig', 'payment']
