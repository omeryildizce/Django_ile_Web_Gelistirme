from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("details", views.details, name="details"),
    path("list", views.liste, name="list "), 
    path("<int:category_id>", views.getProductsByCategoryId),
    path("<str:category>", views.getProductsByCategory, name=
    "products_by_category"),
]