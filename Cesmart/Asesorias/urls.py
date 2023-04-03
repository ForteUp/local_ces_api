from django.urls import path, include

import Asesorias.views
from Asesorias.router import router

# Urls mete las urls de cada vista, y se incluyen las del router

urlpatterns = [
    path('academias/', Asesorias.views.verAcademias),
    path('login/', Asesorias.views.Login),
    path('api/', include(router.urls))
]
