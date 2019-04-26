from django.shortcuts import render
from rest_framework.response import Response
from .models import Roles
from .serializers import Role_Serializer,SignUpSerializer
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth.models import User

# Create your views here.

#Get all Roles
class Roles_View(APIView):
    print ('inside role class')
    def get(self,request):
        roles=Roles.objects.all()
        serializer=Role_Serializer(roles,many=True)
        print (roles)
        return Response({'Roles':serializer.data})


#Sign Up
class SignUp(APIView):
    print ("inside register")
    def post(self,request,format=None):
        
        serializer=SignUpSerializer(data=request.data.get('register'))
        print (serializer)
        if serializer.is_valid():
            print("saved")
            serializer.save()
            return Response({"status":True,"massage":'Data saved successfully'})
        return Response({"status":False,"massage":'Not saved'})
