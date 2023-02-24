from django.db import models


class Band(models.Model):
    band_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    GENRE_CHOICES = (
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Jazz', 'Jazz'),
        ('Country', 'Country'),
        ('Hip Hop', 'Hip Hop'),
        ('R&B', 'R&B'),
        ('Electronic', 'Electronic'),
        ('Classical', 'Classical'),
        ('Reggae', 'Reggae'),
        ('Metal', 'Metal'),
        ('Folk', 'Folk'),
        ('Blues', 'Blues'),
        ('World Music', 'World Music'),
    )
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, null=True)

    def __str__(self):
        return self.band_name


class Venue(models.Model):
    venue_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    MUSIC_TYPES = (
        ('Original Music', 'Original Music'),
        ('Covers', 'Covers'),
        ('Both', 'Both'),
    )
    type_of_music = models.CharField(max_length=50, choices=MUSIC_TYPES)

    def __str__(self):
        return self.venue_name
