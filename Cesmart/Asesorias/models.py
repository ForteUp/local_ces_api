from django.db import models


# Create your models here.

class Asesoria(models.Model):
    estados_asesoria = (
        ("AG", "AGENDADA"),
        ("CA", "CANCELADA"),
        ("RE", "REGISTRADA")
    )
    Fecha = models.DateTimeField()
    Lugar = models.CharField(max_length=50)
    Tema = models.CharField(max_length=50)
    Comentarios = models.TextField()
    Alumno = models.ForeignKey("Alumno", on_delete=models.CASCADE)
    Asesor = models.ForeignKey("Docente", on_delete=models.CASCADE)
    Estado = models.CharField(max_length=2, choices=estados_asesoria, default="AG")


class Docente(models.Model):
    Nombre = models.CharField(max_length=50)
    Correo = models.EmailField(primary_key=True)

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

    def __str__(self):
        return f"0{self.Matricula}"
