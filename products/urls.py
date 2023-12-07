from django.urls import path
from .views import *


urlpatterns = [
    path("",home,name="products"),
    path("createProducts",createProducts,name="createProducts"),
    path("getProduct/<str:id>",getProduct,name="getProduct"),
    path("getProducts",getProducts,name="getProducts"),
    path("createProduct",createProduct,name="createProduct")
]
