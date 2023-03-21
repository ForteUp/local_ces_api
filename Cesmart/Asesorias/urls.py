from django.urls import path, include

import Asesorias.views
from Asesorias.router import router

urlpatterns = [
    path('academias/', Asesorias.views.verAcademias),
    path('login/', Asesorias.views.Login),
    path('api/', include(router.urls))
]
