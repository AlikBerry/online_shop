from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import RequestContext

from shop.forms import ProductForm, CategoryForm
from .models import Category, Product
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'shop/product/list.html',{'category': category,'categories':categories ,'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form=CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def product_create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')

    else:
        form = ProductForm()

    return render(request, 'shop/product/add_product.html', {'form':form})

def category_create_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = CategoryForm()

    return render(request, 'shop/product/add_category.html', {'form':form})