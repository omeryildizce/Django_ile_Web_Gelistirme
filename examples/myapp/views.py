from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Anasayfa")

def details(request):
    return HttpResponse("details")

def liste(request):
    return HttpResponse("list")

def getProductsByCategory(request, category):
    category_text = None
    if category == "bilgisayar":
        category_text = "bilgisayar kategorisindeki ürünler listelendi"
    elif category == "telefon":
        category_text = "telefon kategorisindeki ürünler listelendi"
    else:
        category_text = category + "  sayfası bulunamadı"
    return HttpResponse(category_text)

def getProductsByCategoryId(request, category):
    return HttpResponse(category)