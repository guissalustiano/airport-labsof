# Generated by Django 4.1.3 on 2022-11-25 17:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=32, unique=True)),
                ('city', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'airport',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('website', models.URLField(null=True)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Código unico', max_length=32, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]{3}[0-9]+$', 'Code must be in the format ABC1234')])),
                ('direction', models.CharField(choices=[('A', 'Arrival'), ('D', 'Departure')], default='D', max_length=10)),
                ('time', models.TimeField(help_text='Expected time to arrive or depart')),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.airport')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.company')),
            ],
            options={
                'db_table': 'flight',
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='FlightInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Code for instance, it will concat to flight', max_length=32, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Code must be in the format 1234')])),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Onboarding', 'Onboarding'), ('Taxing', 'Taxing'), ('Departed', 'Departed'), ('Arrived', 'Arrived'), ('Cancelled', 'Cancelled')], default='Scheduled', max_length=32)),
                ('time', models.DateTimeField(help_text='Real flight departure or arrived time')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instance', to='flight.flight')),
            ],
            options={
                'db_table': 'flight_instance',
                'ordering': ['time'],
                'permissions': (('can_list_report', 'List report'), ('can_arrive_report', 'Arrive airport report'), ('can_departure_report', 'Departure airport report'), ('can_status_report', 'Flight Status report')),
            },
        ),
    ]
