from rest_framework.views import APIViews
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import *
from .serializers import *


class RegisterAPUView(APIViews):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username', '').strip()
        email = request.data.get('email', '').strip()
        password = request.data.get('password', '')
        password2 = request.data.get('password2', '')
        

        if not username or not email or not password or not password2:
            return Response(
                {'error': 'Todos los campos son obligatorios.'},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        if password != password2:
            return Response(
                {'error': 'Las contraseñas no coinciden.'},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        if len(password) < 8:
            return Response(
                {'error': 'La contraseña debe tener al menos 8 caracteres.'},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'El nombre de usuario ya está en uso.'},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'El email ya esta registrado.'},
                status=status.HTTP_400_BAD_REQUEST
                )
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
            )
        
        Profile.objects.create(user=user)
        
        serializer = UserSerializer(user)
        return Response(
            {'message': 'Usuario registrado exitosamente.'},
            status=status.HTTP_201_CREATED
            )
        