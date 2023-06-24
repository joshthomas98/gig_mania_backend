from django.db import models
from .choices import GENRE_CHOICES, UK_COUNTRY_CHOICES, UK_COUNTY_CHOICES, ACT_TYPES, ARTIST_TYPES, GIGGING_DISTANCE, USER_TYPES, IS_APPROVED_CHOICES
from multiselectfield import MultiSelectField


class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20, null=True)
    bio = models.CharField(max_length=5000, null=True)
    summary = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, null=True)
    country = models.CharField(
        max_length=50, choices=UK_COUNTRY_CHOICES, null=True)
    county = models.CharField(
        max_length=100, choices=UK_COUNTY_CHOICES, null=True)
    type_of_artist = models.CharField(
        max_length=50, choices=ARTIST_TYPES, null=True)
    image = models.ImageField(
        upload_to='user_profile_images/artist_profile_images/', null=True, blank=True)
    featured_artist = models.BooleanField(default=False)
    facebook = models.CharField(max_length=5000, null=True, blank=True)
    twitter = models.CharField(max_length=5000, null=True, blank=True)
    youtube = models.CharField(max_length=5000, null=True, blank=True)
    artist_membership_type = models.IntegerField(null=True)
    gigging_distance = MultiSelectField(
        choices=GIGGING_DISTANCE, blank=True, max_length=200)

    def __str__(self):
        return self.artist_name


class Unavailability(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='unavailabilities')
    date = models.DateField()

    def __str__(self):
        return f"{self.artist} - {self.date}"


class Venue(models.Model):
    venue_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20, null=True)
    bio = models.CharField(max_length=5000, null=True)
    country = models.CharField(
        max_length=50, choices=UK_COUNTRY_CHOICES, null=True)
    county = models.CharField(
        max_length=100, choices=UK_COUNTY_CHOICES, null=True)
    image = models.ImageField(
        upload_to='user_profile_images/venue_profile_images/', null=True, blank=True)
    type_of_act = models.CharField(
        max_length=100, choices=ACT_TYPES, null=True)
    facebook = models.CharField(max_length=5000, null=True, blank=True)
    twitter = models.CharField(max_length=5000, null=True, blank=True)
    youtube = models.CharField(max_length=5000, null=True, blank=True)
    venue_membership_type = models.IntegerField(null=True)

    def __str__(self):
        return self.venue_name


class ArtistListedGig(models.Model):
    artist_name = models.CharField(max_length=100)
    date_of_gig = models.DateField(null=True)
    venue_name = models.CharField(max_length=100)
    country_of_venue = models.CharField(
        max_length=100, choices=UK_COUNTRY_CHOICES)
    genre_of_gig = models.CharField(
        max_length=50, choices=GENRE_CHOICES, null=True)
    type_of_gig = models.CharField(max_length=50, choices=ACT_TYPES, null=True)
    artist_type = models.CharField(
        max_length=50, choices=ARTIST_TYPES, null=True)
    payment = models.IntegerField(null=True)
    user_type = models.CharField(
        max_length=50, choices=USER_TYPES, null=True)

    def __str__(self):
        date_str = self.date_of_gig.strftime(
            '%d %b %Y') if self.date_of_gig else ''
        return f"{self.artist_name} - {self.venue_name} - {date_str}"


class VenueListedGig(models.Model):
    venue_name = models.CharField(max_length=100)
    date_of_gig = models.DateField(null=True)
    country_of_venue = models.CharField(
        max_length=100, choices=UK_COUNTRY_CHOICES)
    genre_of_gig = models.CharField(
        max_length=50, choices=GENRE_CHOICES, null=True)
    type_of_gig = models.CharField(max_length=50, choices=ACT_TYPES, null=True)
    payment = models.IntegerField(null=True)
    user_type = models.CharField(
        max_length=50, choices=USER_TYPES, null=True)

    def __str__(self):
        date_str = self.date_of_gig.strftime(
            '%d %b %Y') if self.date_of_gig else ''
        return f"{self.venue_name} - {date_str}"


class NewsletterSignup(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email


class MembershipOptions(models.Model):
    membership_id = models.IntegerField(null=True)
    type_of_user = models.CharField(
        max_length=50, choices=USER_TYPES, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000, null=True)
    price = models.CharField(max_length=50, null=True)
    disclosure = models.CharField(max_length=500, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.type_of_user} - {self.title}"


class ArtistWrittenReview(models.Model):
    date_of_performance = models.DateField(null=True)
    artist_name = models.CharField(max_length=100, null=True)
    venue_name = models.CharField(max_length=100, null=True)
    review = models.TextField(max_length=10000, null=True)
    rating = models.IntegerField(null=True)
    is_approved = models.CharField(
        choices=IS_APPROVED_CHOICES, default='Under review', max_length=100, null=True)

    def __str__(self):
        return f"{self.artist_name} || {self.venue_name} || {self.date_of_performance}"


class VenueWrittenReview(models.Model):
    date_of_performance = models.DateField(null=True)
    venue_name = models.CharField(max_length=100, null=True)
    artist_name = models.CharField(max_length=100, null=True)
    review = models.TextField(max_length=10000, null=True)
    rating = models.IntegerField(null=True)
    is_approved = models.CharField(
        choices=IS_APPROVED_CHOICES, default='Under review', max_length=100, null=True)

    def __str__(self):
        return f"{self.venue_name} || {self.artist_name} || {self.date_of_performance}"
