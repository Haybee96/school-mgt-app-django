from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . models import Course
import time

@login_required(login_url='/accounts/login')
def course(request):
    template_name = 'course.html'
    courses = Course.objects.all()
    paginator = Paginator(courses, 10)
    page_number = request.GET.get('page')
    new_courses = paginator.get_page(page_number)
    count = Course.objects.all().count()
    context = {
        'courses': new_courses,
        'count': count,
        'title': 'Courses | School Management App'
    }
    time.sleep(1)
    return render(request, template_name, context)