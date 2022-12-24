from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#    return HttpResponse("Hello")
#
# def about(request):
#    return HttpResponse("Hello Ishan Bhai")

def webpage1(request):
    return render(request, 'index.html')


def webpage2(request):
    return render(request, 'logiin.html')


def webpage3(request):
    return render(request, 'registration.html')


def webpage4(request):
    return HttpResponse(request, 'main.html')


# def pipeline3(request):
#    return HttpResponse("pipeline 3")

