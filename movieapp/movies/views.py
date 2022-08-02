from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Anasayfa")

def movies(request):
    return HttpResponse("Filmler")
    

def movie_details(request, slug):
    return HttpResponse("Film detayı:"+ slug)
    