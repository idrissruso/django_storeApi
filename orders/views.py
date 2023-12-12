from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from .serializer import OrderSerializer
from .models import Order
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

def home(request):
    return HttpResponse("orders")


@api_view(["POST"])
def createOrders(request):
    data = request.data
    try:
        for d in data :
            serializer = OrderSerializer(data=d)
            if serializer.is_valid():
                serializer.save()
        return JsonResponse({"message":"success"},status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({"message":"failed"},status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def getOrders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders,many=True)
    return Response({"message":"success","status":status.HTTP_200_OK,"data":serializer.data})

@api_view(["GET"])
def getOrder(request,id):
    order = Order.objects.get(id=id)
    serializer = OrderSerializer(order)
    return Response({"message":"success","status":status.HTTP_200_OK,"data":serializer.data})
@api_view(["POST"])
def createOrder(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"success"},status=status.HTTP_201_CREATED)
    return Response({"message":"failed"},status=status.HTTP_400_BAD_REQUEST)
