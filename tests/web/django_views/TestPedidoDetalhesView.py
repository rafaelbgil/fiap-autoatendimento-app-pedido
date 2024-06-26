from unittest.mock import Mock, patch
import unittest
from django.test import Client

from src.entities.PedidoFactory import PedidoFactory


class TestPedidoDetalhesView(unittest.TestCase):
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

    @patch('src.web.django_views.PedidoDetalhesView.UseCasePedido')
    def test_obter_pedido(self, mock_use_case_pedido):
        pedido = PedidoFactory.fromDict(self.dicionario_pedido)
        mock_use_case_pedido.obterPedido.return_value = pedido

        client = Client()
        response = client.get('/pedido/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['valor'], 6.9)

    @patch('src.web.django_views.PedidoDetalhesView.UseCasePedido')
    def test_obter_pedido_erro(self, mock_use_case_pedido):
        mock_use_case_pedido.obterPedido.side_effect = Exception('pedido nao encontrado')

        client = Client()
        response = client.get('/pedido/1/')

        self.assertEqual(response.status_code, 404)
