from .models import Bandejatrabajo,Reserva,Usuario,User,Bandeja
from rest_framework import serializers



class BandejatrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandejatrabajo
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BandejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bandeja
        fields = '__all__'