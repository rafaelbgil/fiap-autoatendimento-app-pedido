import unittest
from src.entities.Cliente import Cliente
from src.entities.ClienteFactory import ClienteFactory

class TestClienteFactory(unittest.TestCase):
    def test_client_from_dict(self):
        dicionario_cliente = {
            'nome' : 'Joao Silva',
            'email' : 'joao.silva@teste.com',
            'cpf' : '01234567890',
            'uuid' : '6a125f4f744644aab452db47d1cbce47'
        }

        cliente = ClienteFactory.fromDict(dicionario_cliente=dicionario_cliente)
        self.assertIsInstance(cliente, Cliente)

    def test_client_uuid(self):
        dicionario_cliente = {
            'nome': 'Joao Silva',
            'email': 'joao.silva@teste.com',
            'cpf': '01234567890'
        }

        cliente = ClienteFactory.fromDict(dicionario_cliente=dicionario_cliente)
        cliente.setUuid('6a125f4f-7446-44aa-b452-db47d1cbce47')
        self.assertEqual(cliente.uuid, '6a125f4f744644aab452db47d1cbce47')