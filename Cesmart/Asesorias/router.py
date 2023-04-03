import Asesorias.viewsets as viewsets

from rest_framework import routers
# Los routers generan rutas automaticamente para cada ViewSet
router = routers.DefaultRouter()
router.register('academias', viewsets.AcademiaViewSet)
router.register('alumnos', viewsets.AlumnoViewSet)
router.register('docentes', viewsets.DocenteViewset)
router.register('carreras', viewsets.CarreraViewSet)