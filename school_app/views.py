from django.shortcuts import render, redirect

def home(request):
    template_name = 'index.html'
    context = {
        'title': 'Welcome | School Management App'
    }
    return render(request, template_name, context)