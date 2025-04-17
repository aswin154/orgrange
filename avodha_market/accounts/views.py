from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import SiteSettings


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        messages.info(request, 'Invalid username or password')
        return redirect('login')


    else:
        return render(request, 'login.html', {'no_search': True})


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    settings = SiteSettings.objects.first()

    # see if site settings object exists and create one with default options if it does not exist
    if not settings:
        SiteSettings.objects.create()
        settings = SiteSettings.objects.first()

    if settings.disable_registration:
        messages.warning(request, "Registration disabled, please login using existing credentials.")
        return redirect('login')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email exists')
            return redirect('register')

        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
            user.save()
            print('User created')
            return redirect('login')

    else:
        return render(request, 'register.html')
