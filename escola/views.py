from rest_framework import viewsets
from escola.models import Aluno, Curso
from .serializer import AlunoSerializer, CursoSerializer



class AlunosViewSets(viewsets.ModelViewSet):
    "Exibindo todos os Cursos"
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer




class CursosViewSets(viewsets.ModelViewSet):
    "Exibindo todos os Cursos"
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer