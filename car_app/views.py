from django.shortcuts import render


def index(request):
    return render(request, 'index.html', locals())


def elements(request):
    return render(request, 'elements.html', locals())


def generic(request):
    return render(request, 'generic.html', locals())

