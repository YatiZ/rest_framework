from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        content= serializer.validated_data.get('content')
        
        if content is None:
            content = title
        serializer.save(content = content)
product_list_create_view = ProductListAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product,pk = pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data) 

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        return Response({"invalid":"No Good Data"},status=400)

        

