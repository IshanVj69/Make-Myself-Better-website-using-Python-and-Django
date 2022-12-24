from django.http import HttpResponse
from django.shortcuts import render


def chatapp(request):
    return render(request, 'chat.html')

