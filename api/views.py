from django.shortcuts import render
from .models import Bandejatrabajo,Reserva, Usuario, User,Bandeja
from rest_framework import viewsets
from .serializers import BandejatrabajoSerializer, ReservaSerializer, UsuarioSerializer,UserSerializer,BandejaSerializer
# Create your views here.

class BandejatrabajoViewset(viewsets.ModelViewSet):
    queryset = Bandejatrabajo.objects.all()
    serializer_class = BandejatrabajoSerializer

    def get_queryset(self):
        bandejatrabajo = Bandejatrabajo.objects.all()
        rutempleado =self.request.GET.get('rutempleado')
        if rutempleado:
            bandejatrabajo= bandejatrabajo.filter(rutempleado=rutempleado)
        return bandejatrabajo
        
def home(request):
    return render(request, 'api/home.html')      
    

class ReservaViewset(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def get_queryset(self):
        reserva = Reserva.objects.all()
        rutcliente =self.request.GET.get('rutcliente')
        if rutcliente:
            reserva= reserva.filter(rutcliente=rutcliente)
        return reserva   

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BandejaViewset(viewsets.ModelViewSet):
    queryset = Bandeja.objects.all()
    serializer_class = BandejaSerializer

    def get_queryset(self):
        reserva = Bandeja.objects.all()
        rutempleado =self.request.GET.get('rutempleado')
        if rutempleado:
            reserva= reserva.filter(rutempleado=rutempleado)
        return reserva   