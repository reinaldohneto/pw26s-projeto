from django.contrib import admin
from django.urls import path, include
from pw26s.views import AlunosViewSet, ResponsaveisViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewSet)
router.register(r'responsaveis', ResponsaveisViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
