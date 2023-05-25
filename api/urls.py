from django.urls import path, include
from .views import BandejatrabajoViewset, ReservaViewset,UsuarioViewset,home,UserViewset,BandejaViewset

from rest_framework import routers

router = routers.DefaultRouter()
""" router.register('bandejatrabajo', BandejatrabajoViewset)

router.register('reserva', ReservaViewset)

router.register('Usuario', UsuarioViewset) """

router.register('User', UserViewset)

router.register('Bandeja', BandejaViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('home', home,name="home"),
]