from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CurstoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT1', descricao = 'Curso teste 1', nivel = 'B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso = 'CTT1', descricao = 'Curso teste 1', nivel = 'A'
        )

    def test_requisicao_get(self):
        """Teste para verificar a requisição GET"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post(self):
        """Teste para verificar a requisição POST"""
        dado = {
            'codigo_curso':'CTT',
            'descricao':'Curso Teste',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=dado)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)