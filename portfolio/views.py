from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Portfolio


def index(request):
    projects = Portfolio.objects.order_by('-date_added').filter(show=True)
    paginator = Paginator(projects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'portfolio/index.html', {'projects': page_obj, 'nav': request.resolver_match.url_name})


def project(request, pk):
    project = get_object_or_404(Portfolio, pk=pk, show=True)
    return render(request, 'portfolio/project.html', {'project': project, 'nav': request.resolver_match.url_name})


def posts(request):
    return render(request, 'portfolio/posts.html')
