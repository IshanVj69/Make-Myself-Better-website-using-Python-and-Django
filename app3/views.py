from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.success(request, " Try Again  !!")
            return render(request, 'registration.html')

        else:
          x = User.objects.create_user(username=username, first_name=firstname,
                                       last_name=lastname, email=email, password=password)
          x.save()
          #print("User created")
          messages.success(request, " You have registered successfully !! Now please login.")
          return redirect('/')

    else:
        return render(request, 'registration.html')
