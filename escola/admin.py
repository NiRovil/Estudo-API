from django.contrib import admin
from escola.models import Aluno, Curso

class RegistroAluno(admin.ModelAdmin):
    list_display = ['id','nome', 'cpf', 'data_de_nascimento']
    list_display_links = ['id','nome']
    list_per_page = 5

admin.site.register(Aluno, RegistroAluno)

class RegistroCurso(admin.ModelAdmin):
    list_display = ['id', 'curso']
    list_display_links = ['id', 'curso']
    list_per_page = 5

admin.site.register(Curso, RegistroCurso)