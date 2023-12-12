from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import CategorySerializer
from .models import Category
from django.http import JsonResponse

# Create your views here.
def home(request):
    return HttpResponse("categories")

@api_view(["POST"])
def create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
       
@api_view(["GET"])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(["GET"])
def getCategory(request,id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data,status=status.HTTP_200_OK)