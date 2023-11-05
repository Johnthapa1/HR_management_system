from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from app_rest_api.serializers import EmployeeDesignationSerializer, EmployeeDetailSerializer
from Employees.models import EmployeeDesignation, EmployeeDetail

# Create your views here.
class EmployeeDesignationApiView(APIView):
    def get(self, request):
        designation= EmployeeDesignation.objects.all()
        serializer = EmployeeDesignationSerializer(designation, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        req_data=request.data
    
class EmployeeDetailApiView(APIView):
    def get(self, request):
        detail=EmployeeDetail.objects.all()
        serializer = EmployeeDetailSerializer(detail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        pass