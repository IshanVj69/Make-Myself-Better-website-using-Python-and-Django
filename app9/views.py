from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def Vmotivate(request):
    return render(request, 'Vmotivate.html', {'link': ' http://127.0.0.1:8000/#AuthArticles'})

