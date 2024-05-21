from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.views import APIView

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def post(self, request): 
        # email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        user = authenticate(phone_number=phone_number,password=password)

        if user is not None:
            if user.is_active:
                # Additional actions upon successful login (if needed)
                return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
            else:
                # Inactive user account
                return Response({'message': 'User account is disabled'}, status=status.HTTP_403_FORBIDDEN)
        else:
            # Invalid credentials
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)