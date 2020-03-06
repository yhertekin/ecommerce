from django import forms
from django.forms import ModelForm
from .models import Product
from django.shortcuts import render, redirect


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
