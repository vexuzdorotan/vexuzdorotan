# forms.py
# from django.forms import ModelForm


# admin.py
# admin.ModelAdmin


# settings.py
# LOGIN_URL = '/login'


# views.py
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, logout, authenticate


# ===


from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Portfolio, Technology
from course.models import Course


def index(request):
    technologies = Technology.objects.order_by('rank')

    projects = Portfolio.objects.order_by('-date_added').filter(show=True)
    projects_count = Portfolio.objects.count()
    paginator = Paginator(projects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    courses = Course.objects.all()

    return render(request, 'portfolio/index.html', {
        'technologies': technologies,
        'projects': page_obj,
        'projects_count': projects_count,
        'nav': request.resolver_match.url_name,
        'courses': courses,
    })


def project(request, pk):
    recent_projects = Portfolio.objects.order_by(
        '-date_added').filter(show=True)[:5]
    project = get_object_or_404(Portfolio, pk=pk, show=True)
    return render(request, 'portfolio/project-single.html', {
        'project': project,
        'recent_projects': recent_projects,
        'nav': request.resolver_match.url_name
    })


def posts(request):
    return render(request, 'portfolio/posts.html', {'nav': 'posts'})


# ===== AUTH =====

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:index')

    context = {
        'form': form,
    }
    return render(request, 'portfolio/register.html', context)


def login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)

    context = {
        'form': form,
    }
    return render(request, 'portfolio/login.html', context)
