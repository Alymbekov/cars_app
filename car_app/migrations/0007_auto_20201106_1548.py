# Generated by Django 3.1.3 on 2020-11-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0006_car_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='new',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
