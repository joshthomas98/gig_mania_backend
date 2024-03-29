# Generated by Django 4.1.7 on 2023-06-11 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig_mania_backend', '0061_venue_venue_membership_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_id', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('cost_frequency', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
