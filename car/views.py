from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from car.serializer import BrandSerializer
from rest_framework import generics
from car.models import Brand
from rest_framework import viewsets


class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetail(viewsets.ModelViewSet):
    def get(self, request, pk):
        dsffffsd = Brand.objects.all()
        data = get_object_or_404(Brand, pk=pk)
        serializer = BrandSerializer(data)
        return Response(serializer.data)
