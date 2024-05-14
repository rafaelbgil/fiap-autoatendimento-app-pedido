from unittest.mock import Mock, patch
import unittest
from django.test import Client

from src.entities.Cliente import Cliente
from src.usecases.UseCaseCliente import UseCaseCliente
from src.db.django_orm.ClienteDaoOrm import ClienteDaoOrm


class TestClientView(unittest.TestCase):
    def setUp(self):
        self.cliente1 = Cliente(nome='joao', email='joao@teste.com', cpf='01234567890',
                                uuid='f1794f59-e2c6-4cb9-950a-734828eafde0')
        self.cliente2 = Cliente(nome='lucas', email='lucas@teste.com', cpf='01234567891',
                                uuid='b6114cbb-bb37-4241-b72f-31e2a2e9194d')
        self.lista_clientes = [self.cliente1, self.cliente2]

    @patch('src.web.django_views.ClienteView.UseCaseCliente')
    def test_lista_clientes(self, mock_use_case_cliente):
        mock_use_case_cliente.obterListacliente.return_value = self.lista_clientes
        django_client = Client()
        response = django_client.get('/cliente/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    @patch('src.web.django_views.ClienteView.UseCaseCliente')
    def test_criar_cliente(self, mock_use_case_cliente):
        mock_use_case_cliente.criarCliente.return_value = self.cliente1
        django_client = Client()
        response = django_client.post('/cliente/',
                                      data={'nome': 'joao', 'email': 'joao@teste.com', 'cpf': '01234567890'},
                                      content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['uuid'], 'f1794f59e2c64cb9950a734828eafde0')
