from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def index_view(request):
    return HttpResponse(render(request, 'portfolio/layout.html', { 'nome': 'página' }))


def about_view(request):
    return HttpResponse(f'<p></p>')
