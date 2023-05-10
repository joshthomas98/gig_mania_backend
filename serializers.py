from rest_framework import serializers
from django import forms
from .models import Artist, Availability, Venue, ArtistListedGig
from .choices import UK_COUNTY_CHOICES


class ArtistSerializer(serializers.ModelSerializer):
    gigging_distance = serializers.MultipleChoiceField(
        choices=UK_COUNTY_CHOICES, required=False)

    class Meta:
        model = Artist
        fields = ['id', 'artist_name', 'email', 'username',
                  'password', 'bio', 'genre', 'country', 'county', 'gigging_distance']


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = ['id', 'artist', 'date']


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
