from rest_framework import serializers
from .models import Band, Venue, ArtistListedGig


class BandSerializer(serializers.ModelSerializer):
    genre = serializers.ChoiceField(choices=Band.GENRE_CHOICES)

    class Meta:
        model = Band
        fields = ['id', 'band_name', 'email', 'username',
                  'password', 'genre']


class VenueSerializer(serializers.ModelSerializer):
    type_of_music = serializers.ChoiceField(choices=Venue.MUSIC_TYPES)

    class Meta:
        model = Venue
        fields = ['id', 'venue_name', 'email', 'username',
                  'password', 'type_of_music']


class ArtistListedGigSerializer(serializers.ModelSerializer):
    country_of_venue = serializers.ChoiceField(
        choices=ArtistListedGig.UK_COUNTRIES)
    genre_of_gig = serializers.ChoiceField(
        choices=ArtistListedGig.GENRE_CHOICES)

    class Meta:
        model = ArtistListedGig
        fields = ['id', 'artist_name', 'date_of_gig', 'country_of_venue', 'venue_name',
                  'genre_of_gig', 'payment']
