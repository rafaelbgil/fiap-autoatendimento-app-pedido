import unittest
from unittest.mock import Mock, patch

from src.entities.PedidoFactory import PedidoFactory
from src.entities.Pedido import Pedido
from src.presenters.FormatPedido import FormatPedido

class TestPedidoFactory(unittest.TestCase):
    def setUp(self):
        self.lista_dicionario_item_pedido = [{
            "quantidade": 1,
            "nome": 'Coca Cola',
            "descricao": 'Refrigenrate',
            "preco": 6.9,
            "id_categoria": "4ebf5daa-5758-4ab2-beab-2847d0a280b7",
            "imagem_url": 'https://teste.com.br/refrigerante'
        }]

        self.dicionario_pedido = {
            "id": 1,
            "cpf": "01234567890",
            "lista_itens": self.lista_dicionario_item_pedido,
            "valor": 6.9,
            "status": "aguardando_pagamento"
        }
    def test_criar_pedido(self):
        pedido = PedidoFactory.fromDict(dicionario_pedido=self.dicionario_pedido)
        self.assertIsInstance(pedido, Pedido)
        self.assertEqual(pedido.valor, 6.9)

    def test_formatador_pedido(self):
        pedido = PedidoFactory.fromDict(dicionario_pedido=self.dicionario_pedido)
        pedido_formatado_dict = FormatPedido.fromPedidoToDict(pedido)
        self.assertIsInstance(pedido_formatado_dict, dict)
        self.assertEqual(pedido_formatado_dict['valor'], 6.9)


    def test_formatador_lista_pedido(self):
        pedido = [PedidoFactory.fromDict(dicionario_pedido=self.dicionario_pedido)]
        pedido_formatado_dict = FormatPedido.fromListPedidoToDict(pedido)
        self.assertIsInstance(pedido_formatado_dict, list)
        self.assertIsInstance(pedido_formatado_dict[0], dict)


