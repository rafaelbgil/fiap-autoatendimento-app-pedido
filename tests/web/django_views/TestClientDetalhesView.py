from unittest.mock import Mock, patch
import unittest
from django.test import Client

from src.entities.Cliente import Cliente
from src.usecases.UseCaseCliente import UseCaseCliente
from src.db.django_orm.ClienteDaoOrm import ClienteDaoOrm


class TestClientDetalhesView(unittest.TestCase):
    def setUp(self):
        self.cliente1 = Cliente(nome='joao', email='joao@teste.com', cpf='01234567890',
                                uuid='f1794f59-e2c6-4cb9-950a-734828eafde0')
        self.cliente2 = Cliente(nome='lucas', email='lucas@teste.com', cpf='01234567891',
                                uuid='b6114cbb-bb37-4241-b72f-31e2a2e9194d')


    @patch('src.web.django_views.ClienteDetalhesView.UseCaseCliente')
    def test_obter_cliente(self, mock_use_case_cliente):
        mock_use_case_cliente.obterClient.return_value = self.cliente1
        django_client = Client()
        response = django_client.get('/cliente/f1794f59-e2c6-4cb9-950a-734828eafde0/')

        self.assertEqual(response.status_code, 200)



    @patch('src.web.django_views.ClienteDetalhesView.UseCaseCliente')
    def test_remover_cliente(self, mock_use_case_cliente):
        mock_use_case_cliente.removerCliente.return_value = self.cliente1
        django_client = Client()
        response = django_client.delete('/cliente/f1794f59-e2c6-4cb9-950a-734828eafde0/')

        self.assertEqual(response.status_code, 200)

