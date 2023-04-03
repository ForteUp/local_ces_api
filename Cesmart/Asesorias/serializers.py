from rest_framework import serializers
import Asesorias.models as models

# El serializer convierte de modelo a json
class SerializerAcademia(serializers.ModelSerializer):
    class Meta:
        # Aqui se le indica el modelo
        model = models.Academia
        # Aqui se escogen los atributos a serializar
        fields = '__all__'


class SerializerDocente(serializers.ModelSerializer):
    class Meta:
        model = models.Docente
        fields = '__all__'


class SerializerCarrera(serializers.ModelSerializer):
    # Cuando tenemos llaves foraneas usamos los primary related fields que se serializan el json
    Academia = serializers.PrimaryKeyRelatedField(queryset=models.Academia.objects.all())
    Coordinador = serializers.PrimaryKeyRelatedField(queryset=models.Docente.objects.all())

    class Meta:
        model = models.Carrera
        fields = '__all__'


class SerializerAlumno(serializers.ModelSerializer):
    Asesor = serializers.PrimaryKeyRelatedField(queryset=models.Docente.objects.all())
    Carrera = serializers.PrimaryKeyRelatedField(queryset=models.Carrera.objects.all())

    class Meta:
        model = models.Alumno
        fields = '__all__'
