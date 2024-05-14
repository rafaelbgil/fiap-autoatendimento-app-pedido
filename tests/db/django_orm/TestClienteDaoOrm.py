import unittest
from unittest.mock import Mock, patch
from src.db.django_orm.ClienteDaoOrm import ClienteDaoOrm
from api.models import Cliente as ClienteModel
from src.entities.Cliente import Cliente


class TestClienteDaoOrm(unittest.TestCase):
    def setUp(self):
        self.cliente = ClienteModel()
        self.cliente.uuid = '9aa64580-b904-4db4-becd-725f4baa7c53'
        self.cliente.cpf = '01234567890'
        self.cliente.nome = 'Joao Silva'
        self.cliente.email = 'joao.silva@teste.com.br'

        self.cliente2 = ClienteModel()
        self.cliente2.uuid = '9aa64580-b904-4db4-becd-725f4baa7c54'
        self.cliente2.cpf = '01234567891'
        self.cliente2.nome = 'Joao Neto'
        self.cliente2.email = 'joao.neto@teste.com.br'

    @patch('src.db.django_orm.ClienteDaoOrm.ClienteModel')
    def test_get_client(self, mock_client_model):
        mock_client_model.objects.get.return_value = self.cliente
        retorno_cliente = ClienteDaoOrm.getCliente('9aa64580-b904-4db4-becd-725f4baa7c53')
        self.assertIsInstance(retorno_cliente, Cliente)
        self.assertEqual(retorno_cliente.uuid, '9aa64580b9044db4becd725f4baa7c53')

    @patch('src.db.django_orm.ClienteDaoOrm.ClienteModel')
    def test_list_client(self, mock_client_model):
        mock_client_model.objects.all.return_value = [self.cliente, self.cliente2]
        retorno_lista_clientes = ClienteDaoOrm.listCliente()
        self.assertIsInstance(retorno_lista_clientes, list)
        self.assertIsInstance(retorno_lista_clientes[0], Cliente)

    @patch('src.db.django_orm.ClienteDaoOrm.ClienteModel')
    def test_add_client(self, mock_client_model):
        mock_client_retorno = Mock()
        mock_client_retorno.uuid = '9aa64580-b904-4db4-becd-725f4baa7c53'
        cliente = Cliente(nome='joao', cpf='01234567890', email='teste@joao.com', uuid='9aa64580-b904-4db4-becd-725f4baa7c53')

        retorno_add_cliente = ClienteDaoOrm.addCliente(cliente)
        self.assertIsInstance(retorno_add_cliente, Cliente)
        self.assertEqual(retorno_add_cliente.nome, 'joao')

    @patch('src.db.django_orm.ClienteDaoOrm.ClienteModel')
    def test_delete_client(self, mock_client_model):

        retorno_remover_cliente = ClienteDaoOrm.deleteCliente('9aa64580-b904-4db4-becd-725f4baa7c53')
