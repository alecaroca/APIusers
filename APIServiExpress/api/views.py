from django.shortcuts import render
from rest_framework import viewsets
from .models import Rol,Usuario
from .serializers import RolSerializer, UsuarioSerializer


class RolViewset(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class= RolSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer 

# Create your views here.

def home(request):
    return render(request,'api/home.html')