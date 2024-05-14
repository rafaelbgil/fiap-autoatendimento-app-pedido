from unittest.mock import Mock, patch
import unittest
from django.test import Client

from src.entities.PedidoFactory import PedidoFactory


class TestPedidoAtualizarStatusView(unittest.TestCase):
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
            "status": "recebido"
        }

    @patch('src.web.django_views.PedidoAtualizarStatusView.UseCasePedido')
    def test_atualizar_status_pedido(self, mock_use_case_pedido):
        pedido = PedidoFactory.fromDict(self.dicionario_pedido)
        mock_use_case_pedido.atualizarStatusPedido.return_value = pedido

        client = Client()
        response = client.post('/pedido/1/atualizarStatus/', data={"status": "recebido"},
                               content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['valor'], 6.9)
