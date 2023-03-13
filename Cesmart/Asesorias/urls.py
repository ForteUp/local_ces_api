from django.urls import path, include

import Asesorias.views
from Asesorias.router import router

urlpatterns = [
    path('academias/', Asesorias.views.verAcademias),
    path('api/', include(router.urls))
]
