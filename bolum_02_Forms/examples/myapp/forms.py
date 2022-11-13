from django import forms
class ProductCrteateForm(forms.Form):
    product_name = forms.CharField()
    price = forms.DecimalField()
    description = forms.CharField(widget=forms.Textarea())
    imageUrl = forms.CharField()
    slug = forms.SlugField()