from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('createProduct/', views.createProduct, name="createProduct"),
    path('updateProduct/<str:primary_key>/', views.updateProduct, name="updateProduct"),
    path('deleteProduct/<str:primary_key>/', views.deleteProduct, name="deleteProduct"),
    path('productCreatedSuccess/', views.productCreatedSuccess, name="product_created_success"),
]