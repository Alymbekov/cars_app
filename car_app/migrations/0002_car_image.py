# Generated by Django 3.1.3 on 2020-11-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='car_avatars/'),
        ),
    ]
