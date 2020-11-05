from django.urls import path
from .views import (
    index, elements, generic
)

urlpatterns = [
    path('', index, name='index'),
    path('elements/', elements, name='elements'),
    path('generic/', generic, name='generic'),
]

