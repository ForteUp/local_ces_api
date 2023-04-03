from django.contrib import admin
from .models import *
# Register your models here.

# Aqui se añaden los sitios para el /admin
admin.site.register(Asesoria)
admin.site.register(Academia)
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Carrera)
