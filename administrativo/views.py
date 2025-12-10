from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response #para devolver formato json la respuesta
from rest_framework.decorators import api_view

from administrativo import clave

from .models import Rol,User
from .serializers import RolSerializer, UserSerializer

import google.generativeai as genai


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET']) #no recibe parametros y devuelve informacion
def hola_mundo(request):
    respuesta = { 
        "hola" : "numero 1",
        "nombre" : "erick",
        "profesion" : "docente"
    }
    return Response(respuesta)

@api_view(['POST']) # post recibe parametro y devuelve informacion o realiza una accion
def hola_especifico(request):  
    nombre = request.data.get("nombre")
    return Response({
        "respuesta" : f"hola {nombre} como estas"
    })

##filtrado de informacion 
@api_view(['GET'])
def Usuarios_admin(request, id_rol):
    usuarios = User.objects.filter(rol_id = id_rol)

    data = [
        {
            "id" : usuario.id,
            "username": usuario.username,
            "correo" : usuario.correo
        }
        for usuario in usuarios
    ]
    return Response(data)


##filtrado de informacion usando serializar
@api_view(['GET'])
def Usuarios_ventas(request, id_rol):
    usuarios = User.objects.filter(rol_id = id_rol)
    respuesta = UserSerializer(usuarios, many = True)
    return Response(respuesta.data)


@api_view(['POST'])
def iagemini(request):

    API_KEY = clave.get_clave() # aqui va la api key de gemini
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash"    
    ) 

    dias_disponibles   = request.data.get("dias_disponibles", "")
    horario_disponible = request.data.get("horario_disponible", "")
    materias           = request.data.get("materias", "")
    temas              = request.data.get("temas", "")
    dias               = request.data.get("dias", "")

    prompt = f"""
    tomando en cuenta los datos que te paso a continuacion arma un horario de estudio en formato json con estos atributos" \
    "hora de inicio, hora final, tiempo de estudio, materia, dia de la semana, temas a estudiar de tal manera que sea " \
    "saludable el estudio, tiempo optimo no necesitas tomar todos los horario, basate en la dificultad, tiempos libres para " \
    "mejorar el apredizaje: 

    - Días disponibles: {dias_disponibles}
    - Horario disponible: {horario_disponible}
    - Materias que estudia: {materias}
    - Temas específicos por materia: {temas}
    - Tiempo total disponible: {dias}

    solamente quiero el json, no quiero explicaciones
    """
    response = model.generate_content(prompt )

    return Response(response.text)


@api_view(['POST'])
def iadb(request):
    prompt =  request.data.get("prompt")
    usuarios = User.objects.all()

    texto = ""
    for usuario in usuarios:
        texto += f"[id: {usuario.id}, username: {usuario.username}, correo: {usuario.correo}, id rol: {usuario.rol}]" 


    API_KEY = clave.get_clave() # aqui va la api key de gemini
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash"    
    )
    contexto = "segun esta informacion en formato json " + texto + " responde: "

    response = model.generate_content(contexto + prompt)
    return Response(response.text)

