from django.shortcuts import (
    render, redirect, get_object_or_404
)

from .forms import CarModelForm
from .models import Car


# FBV --- CBV

# FuncitonBasedView --- ClassBasedView

def index(request):
    cars = Car.objects.get_new()
    return render(request, 'index.html', locals())


def car_create(request):
    form = CarModelForm()
    if request.method == 'POST':
        form = CarModelForm(
            request.POST or None, request.FILES or None
        )
        if form.is_valid():
            new_car = form.save()
            return redirect('cars_app:car_details', pk=new_car.pk)
    return render(request, 'cars/car_create.html', locals())


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).first()
    return render(request, 'cars/car_details.html', locals())


def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarModelForm(
        request.POST or None, request.FILES or None,
        instance=car
    )
    if form.is_valid():
        new_car = form.save()
        return redirect(
            'cars_app:car_details', pk=new_car.pk
        )
    return render(request, 'cars/car_edit.html', locals())


def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('cars_app:index')
    return render(request, 'cars/car_delete.html', locals())


def elements(request):
    return render(request, 'elements.html', locals())


def generic(request):
    return render(request, 'generic.html', locals())




def hellow(request):
    return render(request, 'cars/hellow.html', locals())