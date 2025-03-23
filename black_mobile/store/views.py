from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
# @api_view(['GET'])
# def product(request, slug):
#     product = Product.objects.get(slug=slug)
#     serializer = ProductSerializer(product, many=False)
#     return Response(serializer.data)
# @api_view(['POST'])
# def createProduct(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
# @api_view(['PUT'])