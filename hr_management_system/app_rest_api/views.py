from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from app_rest_api.serializers import EmployeeDesignationSerializer, EmployeeDetailSerializer
from Employees.models import EmployeeDesignation, EmployeeDetail

# Create your views here.
class CustomResponse():
    def get_success(self, code, msg, data):
        context = {
            "status_code": code,
            "message": msg,
            "data": data,
            "error": {}
        }
        return context
    
    def get_error(self, code, msg, error):
        context = {
            "status_code": code,
            "message": msg,
            "data": {},
            "error": error
        }
        return context
    
class EmployeeDesignationApiView(APIView):
    def get(self, request):
        designation= EmployeeDesignation.objects.all()
        serializer = EmployeeDesignationSerializer(designation, many=True)
        res = CustomResponse()
        return Response(res.get_success(200, "Designation LIST", serializer.data), status=status.HTTP_200_OK)
        
    def post(self, request):
        req_data=request.data
        serializer= EmployeeDesignationSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDesignationApiPkView(APIView):
    def get_object(self, pk):
        try:
            designation = EmployeeDesignation.objects.get(pk=pk)
            return designation
        except EmployeeDesignation.DoesNotExist:
            return None
            
    def get(self, request, pk):
        instance = self.get_object(pk)
        if instance is None:
            context = {
                "status_code": 200,
                "message": "Designation LIST",
                "data": [],
                "error": {
                    "msg": "Data not found"
                }
                    
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeDesignationSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        instance = self.get_object(pk)
        res = CustomResponse()
        
        if instance is None:
            return Response(res.get_error(404, "Data not found", {"msg":"Data not found"}), status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeDesignationSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_object(pk)
        if instance is None:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg": "Data deleted succesfully"}, status=status.HTTP_200_OK)
    
class EmployeeDetailApiView(APIView):
    def get(self, request):
        detail=EmployeeDetail.objects.all()
        serializer = EmployeeDetailSerializer(detail, many=True)
        res = CustomResponse()
        return Response(res.get_success(200, "Designation LIST", serializer.data), status=status.HTTP_200_OK)
    
    def post(self, request):
        req_data=request.data  #must be a json request
        serializer= EmployeeDetailSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetailApiPKView(APIView):
    def get_object(self, pk):
        try:
            detail = EmployeeDetail.objects.get(pk=pk)
            return detail
        except EmployeeDetail.DoesNotExist:
            return None
    
    def get(self, request, pk):
        instance= self.get_object(pk)
        if instance is None:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer= EmployeeDetailSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, pk):
        instance=self.get_object(pk)
        if instance is None:
            return Response({"ms": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer= EmployeeDetailSerializer(instance=instance, data=request.data, partial=True)
        
        if serializer. is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request, pk):
        instance = self.get_object(pk)
        if instance is None:
            return Response({"ms": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg": "Data deleted succesfully"}, status=status.HTTP_200_OK)
    