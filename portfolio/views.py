import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Area, Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm


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


@login_required()
def new_article_view(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES)
        form.save()

        return redirect('blog')

    return render(request, 'portfolio/new_article.html', context={'form': ArtigoForm()})


def article_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    return render(request, 'portfolio/article.html', context={'artigo': artigo, 'form': ComentarioForm()})


def like_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    artigo.likes += 1
    artigo.save()

    response = HttpResponse(artigo.likes)

    return response


def comment_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)

    form = ComentarioForm(request.POST)
    if not form.is_valid():
        return HttpResponse(status=400)

    comentario = form.save(commit=False)
    comentario.artigo = artigo

    comentario.save()
    form.save_m2m()

    return redirect('article', artigo_id=artigo_id)


def comment_like_view(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    comentario.likes += 1
    comentario.save()

    return HttpResponse(str(comentario.likes))


def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return redirect('login')

        login(request, user)

        return redirect('index')

    return render(request, 'portfolio/login.html')
