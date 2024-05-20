from unittest.mock import Mock, patch
import unittest
from src.usecases.UseCasePedido import UseCasePedido
from src.entities.PedidoFactory import PedidoFactory
from src.entities.Pedido import Pedido


class TestUseCasePedido(unittest.TestCase):
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

    @patch('src.usecases.UseCasePedido.PedidoRepositoryInterface')
    def test_obter_lista_pedidos(self, mock_pedido_repository):
        lista_pedidos = [PedidoFactory.fromDict(dicionario_pedido=self.dicionario_pedido)]
        mock_pedido_repository.listPedido.return_value = lista_pedidos

        retorno_lista = UseCasePedido.obterListaPedidos(mock_pedido_repository)
        self.assertIsInstance(retorno_lista, list)

    """
    @patch('src.usecases.UseCasePedido.PedidoRepositoryInterface')
    def test_criar_pedido(self, mock_pedido_repository):
        pedido = PedidoFactory.fromDict(dicionario_pedido=self.dicionario_pedido)
        mock_pedido_repository.addPedidoFromDict.return_value = pedido

        pedido_retorno = UseCasePedido.criarPedidoFromDict(mock_pedido_repository, self.dicionario_pedido)
        self.assertIsInstance(pedido_retorno, Pedido)
    """
    @patch('src.usecases.UseCasePedido.PedidoRepositoryInterface')
    def test_obter_pedido(self, mock_pedido_repository):
        pedido = PedidoFactory.fromDict(dicionario_pedido=self.dicionario_pedido)
        mock_pedido_repository.getPedido.return_value = pedido

        pedido_retorno = UseCasePedido.obterPedido(mock_pedido_repository, '1')
        self.assertIsInstance(pedido_retorno, Pedido)
