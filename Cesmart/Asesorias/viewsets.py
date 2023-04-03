from django_filters.rest_framework import DjangoFilterBackend
import Asesorias.serializers as serializers
import Asesorias.models as models

from rest_framework import viewsets


class DocenteViewset(viewsets.ModelViewSet):
    queryset = models.Docente.objects.all()
    serializer_class = serializers.SerializerDocente


class AcademiaViewSet(viewsets.ModelViewSet):
    queryset = models.Academia.objects.all()
    serializer_class = serializers.SerializerAcademia


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = models.Alumno.objects.all()
    serializer_class = serializers.SerializerAlumno
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = models.Carrera.objects.all()
    serializer_class = serializers.SerializerCarrera
