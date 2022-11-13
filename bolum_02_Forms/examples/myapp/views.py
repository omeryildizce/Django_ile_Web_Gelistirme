from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product
from .forms import ProductCrteateForm


def index(request):
    products = Product.objects.filter(isActive=True).order_by("-price")

    context = {
        "products": products,
    }

    return render(request, 'index.html', context)


def list(request):
    if "q" in request.GET and request.GET.get('q'):
        q = request.GET['q']
        products = Product.objects.filter(name__contains=q).order_by("-price")
    else:
        products = Product.objects.all().order_by("-price")

    context = {
        "products": products,
    }

    return render(request, 'list.html', context)


def create(request):
    if request.method == 'POST':
        form = ProductCrteateForm(request.POST)
        if form.is_valid():
            p = Product(name=form.cleaned_data["product_name"], description=form.cleaned_data["description"],
                        price=form.cleaned_data["price"], imageUrl=form.cleaned_data["imageUrl"], slug=form.cleaned_data["slug"])
            p.save()
            return HttpResponseRedirect("list")
    else:
        form = ProductCrteateForm()
    return render(request, "create.html", {
        "form": form
    })


def details(request, slug):

    product = get_object_or_404(Product, slug=slug)

    context = {
        "product": product
    }
    return render(request, "details.html", context)
