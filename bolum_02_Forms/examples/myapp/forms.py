from django import forms
from django.forms import widgets
from myapp.models import Product

# class ProductCrteateForm(forms.Form):
#     product_name = forms.CharField(
#         label="Ürün Adı" , min_length=3, max_length=20, error_messages={"min_length": "min 3 karakter giriniz.", "max_length": "mak 20 karakter giriniz."}, widget=forms.TextInput(attrs={"class": "form-control"}))
#     price = forms.DecimalField(label="Fiyat", min_value=10, max_value=10000,
#                                widget=forms.TextInput(attrs={"class": "form-control"}))
#     description = forms.CharField(
#         label="Ürün Açıklaması",  widget=forms.Textarea(attrs={"class": "form-control"}))
#     imageUrl = forms.CharField(
#         label="Fotağraf", widget=forms.TextInput(attrs={"class": "form-control"}))
#     slug = forms.SlugField(label="Url", widget=forms.TextInput(
#         attrs={"class": "form-control"}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "price", "description", "slug")
        # fields = "__all__"
        error_messages = {
            "name":{
                "required":"Bu alan boş bırakılamaz.",
                "max_length":"En fazla 50 karakter girmelisiniz." 
            }
        }
        labels = {
            "name": "Ürün adı",
            "price": "Fiyat",
            "description": "Açıklama",
            "slug": "Url",
        }
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"}),
            "price": widgets.NumberInput(attrs={"class": "form-control"}),
            "description": widgets.Textarea(attrs={"class": "form-control"}),
            "slug": widgets.TextInput(attrs={"class": "form-control"}),
        }
