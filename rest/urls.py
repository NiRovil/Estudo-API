from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import AlunoViewSet, CursoViewSet, MatriculaViewSet, MatriculaAluno

router = routers.DefaultRouter()
router.register('aluno', AlunoViewSet, basename='Alunos')
router.register('curso', CursoViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename='Matricula')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', MatriculaAluno.as_view())
]
