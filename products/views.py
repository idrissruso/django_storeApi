from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from .models import Product
from rest_framework import status
from rest_framework.response import Response

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

@api_view(['GET'])
def getProducts(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        response = {"message": "success", "status": status.HTTP_200_OK,"products": serializer.data,}
        return JsonResponse(response, safe=False)

@api_view(["GET"])
def getProductsPage(request,page):
    products = Product.objects.all()[(page-1)*10:page*10]
    serializer = ProductSerializer(products,many=True)
    return Response({"message":"success","status":status.HTTP_200_OK,"data":serializer.data})


@api_view(["GET"])
def getProduct(request,id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response({"message":"success","status":status.HTTP_200_OK,"data":serializer.data})


@api_view(["POST"])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"success"},status=status.HTTP_201_CREATED)
    return Response({"message":"failed"},status=status.HTTP_400_BAD_REQUEST)