from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('funcionarios/', include('atividades_funcionarios.urls')),
    path('', include('home.urls'))
]
