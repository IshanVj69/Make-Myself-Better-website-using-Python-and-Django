import pyautogui as pu
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def logiin(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        from django.contrib import auth
        x = auth.authenticate(username=username1, password=password1)
        if x is not None:
            auth.login(request, x)
            messages.success(request, " You have login successfully !!")
            return redirect('/')

        else:
            messages.success(request, " Try Again !!")
            return redirect('logiin')

    else:
       return render(request, 'logiin.html')