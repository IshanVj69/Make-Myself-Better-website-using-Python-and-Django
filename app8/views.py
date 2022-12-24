from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

def articles(request):
    return render(request, 'articles.html', {'link': ' http://127.0.0.1:8000/#AuthArticles'})

def webpage1(request):
    return render(request, 'articlema.html', {'link2': 'http://127.0.0.1:8000/app8/articles'})

def webpage2(request):
    return render(request, 'articlemb.html', {'link4': ' http://127.0.0.1:8000/#AuthArticles',
                                              'link5': 'http://127.0.0.1:8000/app8/articles'})

def webpage3(request):
    return render(request, 'articlemc.html', {'link6': ' http://127.0.0.1:8000/#AuthArticles',
                                              'link7': 'http://127.0.0.1:8000/app8/articles'})

def webpage4(request):
    return render(request, 'articlemd.html',{'link8': ' http://127.0.0.1:8000/#AuthArticles',
                                              'link9': 'http://127.0.0.1:8000/app8/articles'})

def Quotes(request):
    return render(request, 'Quotes.html', {'link10': ' http://127.0.0.1:8000/#AuthQuote', })

def Fintips(request):
    return render(request, 'Ftips.html')

def Hintips(request):
    return render(request, 'HTips.html')

def Lintips(request):
    return render(request, 'LTips.html')