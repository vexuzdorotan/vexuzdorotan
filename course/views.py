from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Course


def index(request):
    courses = Course.objects.all().order_by('-date')
    courses_count = Course.objects.count()
    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'courses': page_obj,
        'courses_count': courses_count,
        'nav': request.resolver_match.url_name,
    }

    return render(request, 'course/index.html', context)
