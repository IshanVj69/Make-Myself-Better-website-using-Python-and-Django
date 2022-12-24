from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#    return HttpResponse("Hello")
#
# def about(request):
#    return HttpResponse("Hello Ishan Bhai")

def index(request):
    return render(request, 'index.html', {'link2': 'http://127.0.0.1:8000/login'})


def webpage2(request):
    return render(request, 'logiin.html')


def webpage3(request):
    return render(request, 'registration.html')


def listenc(request):
    return render(request, 'musicd.html')





#def webpage4(request):
#    return HttpResponse(request, 'main.html')
#

# def pipeline3(request):
#    return HttpResponse("pipeline 3")

