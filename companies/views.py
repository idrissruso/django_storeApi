from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializer import CompanySerializer
from .models import Company
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


# Create your views here.
def home(request):
    return HttpResponse("companies")


@api_view(["POST"])
def createCompanies(request):
    data = request.data
    try:
        for d in data :
            serializer = CompanySerializer(data=d)
            if serializer.is_valid():
                serializer.save()
        return Response({"message":"success"})
    except:
        return Response({"message":"failed"})
   
@api_view(["GET"])
def getCompanies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies,many=True)
    return Response({"message":"success","status":status.HTTP_200_OK,"data":serializer.data})
          
@api_view(["GET"])
def getCompany(request,id):
    company = Company.objects.get(id=id)
    serializer = CompanySerializer(company)
    return Response({"message":"success","status":status.HTTP_200_OK,"data":serializer.data})

@api_view(["POST"])
def createCompany(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"success"})
    return Response({"message":"failed"})