# Generated by Django 3.2.8 on 2021-10-18 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('available', models.BooleanField(default=True)),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'destination',
                'verbose_name_plural': 'destinations',
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.destination')),
            ],
            options={
                'verbose_name': 'travel',
                'verbose_name_plural': 'travels',
            },
        ),
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Birth_date', models.DateField()),
                ('document_id', models.IntegerField(unique=True)),
                ('type_of_document', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=30)),
                ('travel', models.ManyToManyField(to='trips.Travel')),
            ],
            options={
                'verbose_name': 'passanger',
                'verbose_name_plural': 'passangers',
            },
        ),
    ]
