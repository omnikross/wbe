from django.shortcuts import render
from rest_framework import status
from .serializers import LoginSerializer, RegistrationSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from .models import User
from rest_framework.renderers import TemplateHTMLRenderer

class RegistrationAPIView(APIView):
  
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    
    def post(self, request):
   
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )
    

class LoginAPIView(APIView):
   
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)      