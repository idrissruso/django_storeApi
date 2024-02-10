from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
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
        response = {"message":"success","status":status.HTTP_201_CREATED,"data":serializer.data}
        return JsonResponse(response,safe=False)
    return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
       
@api_view(["GET"])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories,many=True)
    response = {"message":"success","status":status.HTTP_200_OK,"data":serializer.data}
    return JsonResponse(response,safe=False)

@api_view(["GET"])
def getCategory(request,id):
    category = Category.objects.get(id=id)
    serializer = CategorySerializer(category)
    response = {"message":"success","status":status.HTTP_200_OK,"data":serializer.data}
    return JsonResponse(response,safe=False)