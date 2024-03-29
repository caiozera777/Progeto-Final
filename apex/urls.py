from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSets,CursosViewSets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('alunos', AlunosViewSets, basename = 'aluno')
router.register('cursos', CursosViewSets, basename = 'curso')


urlpatterns = [
path('admin/', admin.site.urls),
path('', include(router.urls)),
]
