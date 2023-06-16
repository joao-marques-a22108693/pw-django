import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Area, Artigo, Comentario, Projeto, TFC, Banda
from .forms import ArtigoForm, ComentarioForm


# Create your views here.

def blog_view(request):
    areas = Area.objects.all()
    return render(request, 'portfolio/blog.html', context={'areas': areas})


def index_view(request):
    return render(request, 'portfolio/index.html', context={'projects': Projeto.objects.all(), 'tfcs': TFC.objects.all()})


def playground_view(request):
    return render(request, 'portfolio/playground.html')


def admin_view(request):
    return render(request, 'portfolio/admin.html')


@login_required()
def new_article_view(request):
    if request.method == "POST":
        form = ArtigoForm(request.POST, request.FILES)

        if not form.is_valid():
            return HttpResponse(status=400)

        form.save()

        return redirect('blog')

    return render(request, 'portfolio/new_article.html', context={'form': ArtigoForm()})


@login_required()
def edit_article_view(request, artigo_id):
    if request.method == "POST":
        inst = get_object_or_404(Artigo, id=artigo_id)
        form = ArtigoForm(request.POST, request.FILES, instance=inst)

        if not form.is_valid():
            return HttpResponse(status=400)

        form.save()

        return redirect('article', artigo_id=artigo_id)

    inst = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'portfolio/edit_article.html', context={'form': ArtigoForm(instance=inst), 'artigo': inst})


@login_required()
def delete_article_view(request, artigo_id):
    obj = get_object_or_404(Artigo, id=artigo_id)
    obj.delete(keep_parents=True)
    return redirect('blog')


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


@csrf_exempt
def login_view(request, url='index'):
    if request.method == 'POST' and request.POST.get('username', None) and request.POST.get('password', None):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if type(user) is not User:
            return render(request, 'portfolio/login.html', context={'next': request.POST.get('next', None)})

        login(request, user)

        return redirect(request.POST['next'] if request.POST.get('next', None) else url)

    return render(request, 'portfolio/login.html', context={'next': request.GET.get('next', None)})
