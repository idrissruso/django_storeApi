from django.urls import path
from .views import *


urlpatterns = [
    path("",home,name="orders"),
    path("createOrders",createOrders,name="createOrders"),
    path("getOrder/<str:id>",getOrder,name="getOrder"),
    path("getOrders",getOrders,name="getOrders"),
    path("createOrder",createOrder,name="createOrder")
    
]
