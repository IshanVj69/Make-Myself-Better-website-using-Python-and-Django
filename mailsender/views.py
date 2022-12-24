from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def mailform(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')
        print(sub, msg, email)
        send_mail(sub, msg, 'ishanvijay6@gamil.com', [email])
        return HttpResponse('email send that !')
    return render(request, 'mailform.html', {'link3': ' http://127.0.0.1:8000/'})
