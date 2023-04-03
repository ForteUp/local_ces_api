from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

import Asesorias.models as models
import Asesorias.serializers as serializers
import rest_framework.viewsets as viewsets
from rest_framework import mixins, status


#
# class Prueba(mixins.CreateModelMixin):
#     queryset = models.Alumno.objects.all()
#     serializer_class = serializers.SerializerAlumno


@api_view(['GET'])
def verAcademias(request):
    queryset = models.Alumno.objects.all()
    return Response(serializers.SerializerAlumno(queryset, many=True).data)


@api_view(['POST'])
def Login(request):
    correo = request.data['Correo']
    password = request.data['Password']
    print(correo, password)
    try:
        query = models.Alumno.objects.get(Matricula=correo)
        print(query.Password)
        if password == query.Password:
            estudiante = serializers.SerializerAlumno(query).data
            estudiante['tipo'] = 'estudiante'
            return Response(estudiante, status=status.HTTP_200_OK)
        else:
            return Response({'Contraseña incorrecta': '200'}, status=status.HTTP_404_NOT_FOUND)
    except models.Alumno.DoesNotExist:
        try:
            query = models.Docente.objects.get(Correo=correo)
            if password == query.Password:
                asesor = serializers.SerializerDocente(query).data
                asesor['tipo'] = 'asesor'
                return Response(asesor, status=status.HTTP_200_OK)
            else:
                return Response({'Contraseña': '200'}, status=status.HTTP_404_NOT_FOUND)
        except models.Docente.DoesNotExist:
            return Response({'No existe': '200'}, status=status.HTTP_404_NOT_FOUND)
