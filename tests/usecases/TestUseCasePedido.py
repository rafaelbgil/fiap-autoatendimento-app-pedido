from unittest.mock import Mock, patch
import unittest
from src.usecases.UseCasePedido import UseCasePedido
from src.entities.PedidoFactory import PedidoFactory


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

        UseCasePedido.obterListaPedidos(mock_pedido_repository)


