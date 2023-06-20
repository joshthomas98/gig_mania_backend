# Generated by Django 4.1.7 on 2023-06-12 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0062_membershipoptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipoptions',
            name='type_of_user',
            field=models.CharField(choices=[('Artist', 'Artist'), ('Venue', 'Venue')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='membershipoptions',
            name='description',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]