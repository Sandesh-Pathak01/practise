from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def loginpage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        log_in = authenticate(username=username, password=password)

        if log_in is not None:
            login(request, log_in)
            return redirect('homepage')
        else:
            messages.info(request, 'Login Failed Check Pass And Email Carefullly.')

    return render(request, 'loginpage.html')


def signuppage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username = username).exists():
            messages.info(request, 'Username Is Taken PLease Try Another.')
        else:
            new_user = User.objects.create_user(username = username, password = password, email = email)
            login(request, new_user)
            messages.info(request, 'Account Created Succesfully PLease Complete Your Details.')
            return redirect('/')


    return render(request, 'signuppage.html')


def logoutt(request):

    logout(request)
    return redirect('homepage')