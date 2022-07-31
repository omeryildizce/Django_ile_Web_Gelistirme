from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Anasayfa")

def details(request):
    return HttpResponse("details")

def liste(request):
    return HttpResponse("list")
