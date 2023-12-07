from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="companies"),
    path("createCompanies/",createCompanies,name="createCompanies"),
    path("getCompany/<str:id>",getCompany,name="getCompany"),
    path("getCompanies",getCompanies,name="getCompanies"),
    path("createCompany",createCompany,name="createCompany")
]
