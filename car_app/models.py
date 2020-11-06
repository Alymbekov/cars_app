import os
import random

from django.db import models
from django.db.models import Count


def get_filename_ext(filepath):
    # /..../helloworld.jpg
    #helloworld.jpg
    base_name = os.path.basename(filepath)
    #helloworld-> name
    #jpg --> ext
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename= random.randint(1, 9999999999)
    name, ext = get_filename_ext(filename)
    print(name, ext)
    final_converted_name = "{new_filename}{ext}".format(
        new_filename=new_filename, ext=ext
    )
    #9939393932.jpg
    print("final function")
    print(final_converted_name)
    print("cars/{new_filename}/{final_converted_name}".format(
        new_filename=new_filename, final_converted_name=final_converted_name
    ))
    return "cars/{new_filename}/{final_converted_name}".format(
        new_filename=new_filename, final_converted_name=final_converted_name
    )


class CustomCarQuerySet(models.query.QuerySet):
    def get_new(self):
        return self.filter(new=True).order_by('id')[:6]


class CarsManager(models.Manager):
    def get_queryset(self):
        return CustomCarQuerySet(self.model, using=self._db)

    def get_new(self):
        return self.get_queryset().get_new()


class Car(models.Model):
    title = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(
        default=1991
    )
    model = models.CharField(
        max_length=100
    )
    odometer = models.PositiveIntegerField(
        default=0
    )
    objects = CarsManager()
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True
    )
    new = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"{self.title} -> {self.odometer}"

# 234324sfd.jpg


