from unittest.mock import Mock, patch
import unittest

from django.test import Client


class TestCriarUsuarioView(unittest.TestCase):
    @patch('src.web.django_views.CriarUsuarioView.UseCaseCriarUsuario')
    def test_criar_usuario(self, mock_use_case_criar_usuario):
        dicionario_usuario = {
            "nome": "Joao silva",
            "email": "joao@teste.com.br",
            "cpf": "01234567890",
            "senha": "abc123456@"
        }
        mock_use_case_criar_usuario.criar.return_value = dicionario_usuario

        client = Client()
        response = client.post('/criar_usuario/', data=dicionario_usuario, content_type='application/json')

        self.assertEqual(response.status_code, 200)
