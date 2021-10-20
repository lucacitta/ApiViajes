# Generated by Django 3.2.8 on 2021-10-20 13:45

from django.db import migrations, models


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
                ('available', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField()),
                ('activate', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'destination',
                'verbose_name_plural': 'destinations',
            },
        ),
    ]