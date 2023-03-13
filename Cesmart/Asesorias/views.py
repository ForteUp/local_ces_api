from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

import Asesorias.models as models
import Asesorias.serializers as serializers
import rest_framework.viewsets as viewsets
from rest_framework import mixins

#
# class Prueba(mixins.CreateModelMixin):
#     queryset = models.Alumno.objects.all()
#     serializer_class = serializers.SerializerAlumno


@api_view(['GET'])
def verAcademias(request):
    queryset = models.Alumno.objects.all()
    return Response(serializers.SerializerAlumno(queryset, many=True).data)
