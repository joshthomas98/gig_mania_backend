# Generated by Django 4.1.7 on 2023-06-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0069_remove_gig_advertiser_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='venue_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]