from django.shortcuts import render


def Videos(request):
    return render(request, 'Videos.html', {'link': ' http://127.0.0.1:8000/#AuthArticles'})

