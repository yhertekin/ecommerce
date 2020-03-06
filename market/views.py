from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
# Create your views here.



def index(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'market/index.html', context)


def createProduct(request):
    form = ProductForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_created_success')
    return render(request, 'market/createProduct.html', context)

def productCreatedSuccess(request):
    return render(request, 'market/product_created_success.html')

def updateProduct(request, primary_key):
    product = Product.objects.get(id=primary_key)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'market/updateProduct.html', context)

def deleteProduct(request, primary_key):
    product = Product.objects.get(id=primary_key)
    if request.method == 'POST':
        product.delete()
        return redirect('/')
    context = {'product': product}
    return render(request, "market/deleteProduct.html", context)