from Asesorias.viewsets import AcademiaViewSet, AlumnoViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register('academias', AcademiaViewSet)
router.register('alumnos', AlumnoViewSet)