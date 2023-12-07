from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="categories"),
    path("create",create,name="create"),
    path("getCategories",getCategories,name="getCategories"),
    path("getCategory/<str:id>",getCategory,name="getCategory")
]
