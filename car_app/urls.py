from django.urls import path
from . import views

app_name = 'cars_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('elements/', views.elements, name='elements'),
    path('generic/', views.generic, name='generic'),
    path('cars/create/', views.car_create, name='car_create'),
    path('cars/<int:pk>/', views.car_details, name='car_details'),
    path('cars/<int:pk>/edit/', views.car_edit, name='car_edit'),
    path('cars/<int:pk>/delete/', views.car_delete, name='car_delete'),
]

