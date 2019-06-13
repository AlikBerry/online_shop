from django import forms

from shop.models import Category, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'image',
            'description',
            'price',
            'available',

        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]