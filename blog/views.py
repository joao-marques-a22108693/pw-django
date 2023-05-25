from django.http import HttpResponse
from django.shortcuts import render

from .models import Area


# Create your views here.

def index_view(request):
    areas = Area.objects.all()
    return render(request, 'blog/index.html', context={'areas': areas})
