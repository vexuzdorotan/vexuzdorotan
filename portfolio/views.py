from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Portfolio, Technology
from course.models import Course


def index(request):
    technologies = Technology.objects.order_by('-rank').filter(show=True)

    projects = Portfolio.objects.order_by('-date_added').filter(show=True)
    projects_count = Portfolio.objects.count()
    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    courses = Course.objects.all().order_by('-date').filter(show=True)[:3]
    courses_count = Course.objects.count()

    return render(request, 'portfolio/index.html', {
        'technologies': technologies,
        'projects': page_obj,
        'projects_count': projects_count,
        'nav': request.resolver_match.url_name,
        'courses': courses,
        'courses_count': courses_count,
    })


def projects(request):
    projects = Portfolio.objects.order_by('-date_added').filter(show=True)
    projects_count = Portfolio.objects.count()
    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'projects': page_obj,
        'projects_count': projects_count,
        'nav': request.resolver_match.url_name,
    }
    return render(request, 'portfolio/projects.html', context)


def project(request, pk):
    recent_projects = Portfolio.objects.order_by(
        '-date_added').filter(show=True)[:5]
    project = get_object_or_404(Portfolio, pk=pk, show=True)
    return render(request, 'portfolio/project-single.html', {
        'project': project,
        'recent_projects': recent_projects,
        'nav': request.resolver_match.url_name
    })
