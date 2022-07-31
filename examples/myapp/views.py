from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render

data = {
    "telefon":"telefon kategorisindeki ürünler listelendi",
    "bilgisayar":"bilgisayar kategorisindeki ürünler listelendi",
    "elektronik":"elektronik kategorisindeki ürünler listelendi"
}


def index(request):
    return HttpResponse("Anasayfa")

def details(request):
    return HttpResponse("details")

def liste(request):
    return HttpResponse("list")


def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id <= len(category_list) & category_id >= 0:
        redirect_text = category_list[category_id - 1]
        return redirect("/products/"+redirect_text)
    else:
        return HttpResponseNotFound("yanlış kategori seçimi yapıldı")

def getProductsByCategory(request, category):
    try:
        category_text = data[category]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi yapıldı")            
