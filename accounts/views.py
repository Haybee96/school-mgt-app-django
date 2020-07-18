from django.shortcuts import render, redirect
from django.contrib import messages, auth
import time


def login(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # If user exists in database, authenticate and log user in
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            time.sleep(4)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credential(s)')
            time.sleep(1)
            return redirect('login')
    else:
        return render(request, template_name, {'title': 'Login | School Management App'})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        time.sleep(1)
        return redirect(login)