# Generated by Django 4.1.7 on 2023-06-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0079_artistwrittenreview_artist_review_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueWrittenReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_performance', models.DateField(null=True)),
                ('artist_name', models.CharField(max_length=100, null=True)),
                ('artist_review', models.TextField(max_length=10000, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='artistwrittenreview',
            old_name='artist_review',
            new_name='review',
        ),
        migrations.AddField(
            model_name='artistwrittenreview',
            name='venue_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]