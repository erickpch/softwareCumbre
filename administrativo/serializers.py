from rest_framework import serializers
from .models import Rol, User


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol 
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    rol_id = serializers.PrimaryKeyRelatedField( 
                queryset = Rol.objects.all(),
                source = 'rol',
                write_only = True
            )
    rol = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = User
        fields = ['id', 'username', 'foto', 'correo', 'rol_id', 'rol']
        extra_kwargs = {
            'password': {'write_only': True}
        }