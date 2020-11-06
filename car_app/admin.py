from django.contrib import admin
from django.contrib.admin import register

from .models import Car


@register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
         'title',
        'odometer', 'year', 'model'
    )
    list_display_links = ('title', 'model')
    list_filter = ('year', 'model')
    search_fields = ('title', 'model')




