from django.shortcuts import render, redirect

from .models import Area
from .forms import ArtigoForm


# Create your views here.

def index_view(request):
    areas = Area.objects.all()
    return render(request, 'portfolio/index.html', context={'areas': areas})


def admin_view(request):
    return render(request, 'portfolio/admin.html')


def new_article_view(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST)
        form.save()

        return redirect('index')

    return render(request, 'portfolio/new_article.html', context={'form': ArtigoForm()})
