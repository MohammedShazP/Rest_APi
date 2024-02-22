from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegister
from rest_framework.response import Response
from rest_framework import status
from . models import Users

# Create your views here.

class Register(APIView):
    def get(self,request):
        user = Users.objects.all()
        serializer = UserRegister(user,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserRegister(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get(self,request,id):
        user = Users.objects.get(id = id)
        serializer = UserRegister(user)
        return Response(serializer.data)

    def put(self,request,id):
        user = Users.objects.get(id=id)
        serializer = UserRegister(user,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        user = Users.objects.get(id = id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
