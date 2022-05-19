from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, AlunoMatriculaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class MatriculaAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = AlunoMatriculaSerializer