from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "isActive", "slug")
    list_display_links = ("name", "price")
    readonly_fields = ("slug", )
    list_filter = ("name", "price", "category",)
    list_editable = ("isActive",)
    search_fields = ("name",)
admin.site.register(Product, ProductAdmin)