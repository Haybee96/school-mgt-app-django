from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . models import Student
import time

@login_required(login_url='/accounts/login')
def student(request): 
    template_name = 'student.html'
    students = Student.objects.all()
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    new_students = paginator.get_page(page_number)
    count = Student.objects.all().count()
    context = {
        'students': new_students,
        'count': count,
        'title': 'Students | School Management App',
    }
    time.sleep(1)
    return render(request, template_name, context)
