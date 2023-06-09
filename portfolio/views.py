from django.shortcuts import render, redirect

from .models import Area
from .forms import ArtigoForm


# Create your views here.

def blog_view(request):
    areas = Area.objects.all()
    return render(request, 'portfolio/blog.html', context={'areas': areas})


def index_view(request):
    return render(request, 'portfolio/index.html')


def playground_view(request):
    return render(request, 'portfolio/playground.html')


def admin_view(request):
    return render(request, 'portfolio/admin.html')


def new_article_view(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST)
        form.save()

        return redirect('index')

    return render(request, 'portfolio/new_article.html', context={'form': ArtigoForm()})
