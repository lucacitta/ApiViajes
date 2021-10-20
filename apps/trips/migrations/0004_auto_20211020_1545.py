# Generated by Django 3.2.8 on 2021-10-20 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
        ('trips', '0003_alter_travel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinations.destination'),
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
    ]