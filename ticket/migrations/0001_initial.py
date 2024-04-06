# Generated by Django 5.0.4 on 2024-04-04 22:14

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('hall', models.CharField(max_length=30)),
                ('duration', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('time', models.CharField(choices=[('12-pm', '12-pm'), ('3-pm', '3-pm'), ('6-pm', '6-pm'), ('9-pm', '9-pm'), ('12-am', '12-am')], max_length=5)),
                ('price', models.FloatField()),
                ('guest_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest_name', to='ticket.guest')),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_name', to='ticket.movie')),
            ],
        ),
    ]