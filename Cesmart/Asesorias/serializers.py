from rest_framework import serializers
import Asesorias.models as models


class SerializerAcademia(serializers.ModelSerializer):
    class Meta:
        model = models.Academia
        fields = '__all__'


class SerializerDocente(serializers.ModelSerializer):
    class Meta:
        model = models.Docente
        fields = '__all__'


class SerializerCarrera(serializers.ModelSerializer):
    Academia = serializers.StringRelatedField()
    Coordinador = serializers.StringRelatedField()

    class Meta:
        model = models.Carrera
        fields = '__all__'


class SerializerAlumno(serializers.ModelSerializer):
    Asesor = SerializerDocente()
    Carrera = SerializerCarrera()

    class Meta:
        model = models.Alumno
        fields = '__all__'

