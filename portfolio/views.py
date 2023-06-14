from django.shortcuts import render, redirect, get_object_or_404

from .models import Area, Artigo
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
        form = ArtigoForm(request.POST, request.FILES)
        form.save()

        return redirect('index')

    return render(request, 'portfolio/new_article.html', context={'form': ArtigoForm()})


def article_view(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    return render(request, 'portfolio/article.html', context={'artigo': artigo})
