from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RolViewSet, UserViewSet
from . import views


router = DefaultRouter()
router.register(r'roles',RolViewSet)
router.register(r'users',UserViewSet)



urlpatterns = [
    path('', include(router.urls) ),

    
    path('hola/', views.hola_mundo),
    path('hola2/', views.hola_especifico),
    path('userAdmin/<int:id_rol>', views.Usuarios_admin),
    path('userVenta/<int:id_rol>', views.Usuarios_ventas),
    

    path('ia', views.iagemini),
    path('iadb', views.iadb),

    path('pais', views.traerPais)

]