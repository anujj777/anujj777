from django.shortcuts import render
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class TeacherAPI(APIView):
 def get(self, request, pk=None, format=None):
  id = pk
  if id is not None:
   Tea = Teacher.objects.get(id=id)
   serializer = TeacherSerializer(Tea)
   print(serializer.data) # Native python data
   return Response(serializer.data)

  Tea = Teacher.objects.all()
  serializer = TeacherSerializer(Tea, many=True)
  return Response(serializer.data)
 
 def post(self,request,format=None):
  print(request.data)
  serializer = TeacherSerializer(data=request.data)
  print(serializer)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
  return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      
 def put(self, request, pk, format=None):
  id = pk
  Tea = Teacher.objects.get(id=id)
  serializer = TeacherSerializer(Tea,data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'complete data updated'})
  return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

 def patch(self, request, pk, format=None):
  id = pk
  Tea = Teacher.objects.get(id=id)
  serializer = TeacherSerializer(Tea,data=request.data,partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'partial data updated'})
  return Response(serializer.errors)

 def delete(self, request, pk, format=None):
  id = pk
  Tea = Teacher.objects.get(id=id)
  Tea.delete()
  return Response({'msg':'data is deleted'})  

  

 

 

 
