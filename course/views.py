from django.shortcuts import render
from .models import Course


def index(request):
    courses = Course.objects.all().order_by('-date')

    context = {
        'courses': courses,
    }

    return render(request, 'course/index.html', context)
