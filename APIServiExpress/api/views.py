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

    def get_queryset(self):
        usuario = Usuario.objects.all()
        email =self.request.GET.get('email')
        if email:
            usuario= usuario.filter(email=email)
        return usuario

# Create your views here.

def home(request):
    return render(request,'api/home.html')