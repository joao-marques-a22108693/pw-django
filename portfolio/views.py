import json

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


def new_article_view(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES)
        form.save()

        return redirect('index')

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

    response = HttpResponse(json.dumps({'texto': form.texto, 'autor': form.autor}))

    return response
