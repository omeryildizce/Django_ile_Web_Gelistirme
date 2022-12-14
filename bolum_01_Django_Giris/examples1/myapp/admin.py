from django.contrib import admin
from .models import Category, Product, Address, Supplier

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "isActive", "slug", "selected_categories")
    list_display_links = ("name", "price")
    prepopulated_fields = {"slug": ("name",) }
    list_filter = ("name", "price", "categories" )
    list_editable = ("isActive",)
    search_fields = ("name",)

    def selected_categories(self, obj):
        html = ""

        for category in obj.categories.all():
            html += category.name + " "
        return html

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Supplier)