# Generated by Django 3.1.3 on 2020-11-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0003_auto_20201106_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='cars/'),
        ),
    ]
