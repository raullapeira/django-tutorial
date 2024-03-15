from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

def index(request):
    print("El tipo de request es", type(request))
    return HttpResponse("<script>console.log('paco')</script><b>Hello, world.</b><img src='gato.jpg' alt='no esta'> You're at the polls index.")

