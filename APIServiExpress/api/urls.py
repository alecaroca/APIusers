from django.urls import path, include
from .views import home,RolViewset,UsuarioViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('rol', RolViewset)
router.register('usuario', UsuarioViewset)



urlpatterns = [
    path('', home, name="home"),
    path('api/', include(router.urls)),
]
