from django.db import models
# import hashlib

# Create your models here.

# Aqui se agregan los modelos


class Asesoria(models.Model):
    # Estas son las opciones posibles para el field Estado
    estados_asesoria = (
        ("AG", "AGENDADA"),
        ("CA", "CANCELADA"),
        ("RE", "REGISTRADA")
    )
    # Aqui agregamos los atributos del modelo, que son las columnas de la tabla
    Fecha = models.DateTimeField() #Fecha y hora
    Lugar = models.CharField(max_length=50) #Varchar de 50
    Tema = models.CharField(max_length=50) #Varchar de 50
    Comentarios = models.TextField() #Texto
    # Estas son las llaves foraneas, hacen referencia a otros modelos, o en este caso tablas
    Alumno = models.ForeignKey("Alumno", on_delete=models.CASCADE)
    Asesor = models.ForeignKey("Docente", on_delete=models.CASCADE)
    Estado = models.CharField(max_length=2, choices=estados_asesoria, default="AG")


class Docente(models.Model):
    Nombre = models.CharField(max_length=50)
    #Aqui correo se define como una superclave
    Correo = models.EmailField(primary_key=True)
    Password = models.CharField(max_length=10)

    # Esta es la representacion del modelo
    def __str__(self):
        return f"{self.Correo}"


class Carrera(models.Model):
    Nombre = models.CharField(max_length=50, primary_key=True)
    Academia = models.ForeignKey("Academia", on_delete=models.CASCADE)
    Coordinador = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Nombre}"


class Academia(models.Model):
    Nombre = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f"{self.Nombre}"


class Alumno(models.Model):
    Matricula = models.PositiveIntegerField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Asesor = models.ForeignKey(Docente, on_delete=models.CASCADE)
    Carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    Password = models.CharField(max_length=10)
    def __str__(self):
        return f"0{self.Matricula}"
