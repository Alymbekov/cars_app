# Generated by Django 3.1.3 on 2020-11-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField(default=1991)),
                ('model', models.CharField(max_length=100)),
                ('odometer', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
