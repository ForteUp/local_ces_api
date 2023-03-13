from Asesorias.serializers import SerializerAcademia, SerializerAlumno
from Asesorias.models import Academia, Alumno

from rest_framework import viewsets


class AcademiaViewSet(viewsets.ModelViewSet):
    queryset = Academia.objects.all()
    serializer_class = SerializerAcademia


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = SerializerAlumno
