from django import forms


class ProductCrteateForm(forms.Form):
    product_name = forms.CharField(
        label="Ürün Adı", required=False, min_length=3, max_length=20, error_messages={"min_length": "min 3 karakter giriniz.", "max_length": "mak 20 karakter giriniz."})
    price = forms.DecimalField(label="Fiyat", min_value=10, max_value=10000)
    description = forms.CharField(
        label="Ürün Açıklaması", widget=forms.Textarea())
    imageUrl = forms.CharField(label="Fotağraf")
    slug = forms.SlugField(label="Url")
