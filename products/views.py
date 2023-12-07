from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from .models import Product
from rest_framework import status

# Create your views here.

def home(request):
    return HttpResponse("products")

@api_view(["POST"])
def createProducts(request):
    data = request.data
    try:
        for d in data :
            serializer = ProductSerializer(data=d)
            if serializer.is_valid():
                serializer.save()
        return JsonResponse({"message":"success"},status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({"message":"failed"},status=status.HTTP_400_BAD_REQUEST)

def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return JsonResponse({"message":"success","status":status.HTTP_200_OK,"data":serializer.data},safe=False)

def getProduct(request,id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return JsonResponse({"message":"success","status":status.HTTP_200_OK,"data":serializer.data},safe=False)


@api_view(["POST"])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message":"success"},status=status.HTTP_201_CREATED)
    return JsonResponse({"message":"failed"},status=status.HTTP_400_BAD_REQUEST)