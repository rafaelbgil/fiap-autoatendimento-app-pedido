from unittest.mock import Mock, patch
import unittest
from django.test import Client

from src.entities.PedidoFactory import PedidoFactory


class TestPedidoView(unittest.TestCase):
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

    @patch('src.web.django_views.PedidoView.UseCasePedido')
    def test_obter_lista_pedidos(self, mock_use_case_pedido):
        lista_pedidos = [PedidoFactory.fromDict(self.dicionario_pedido)]
        mock_use_case_pedido.obterListaPedidos.return_value = lista_pedidos

        client = Client()
        response = client.get('/pedido/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['valor'], 6.9)

    @patch('src.web.django_views.PedidoView.PedidoRepositoryOrm')
    def test_adicionar_pedido_sem_autenticacao(self, mock_pedido_repository):
        mock_pedido_repository.addPedidoFromDict.return_value = PedidoFactory.fromDict(self.dicionario_pedido)
        client = Client()
        response = client.post('/pedido/', data=self.dicionario_pedido, content_type='application/json')
        self.assertEqual(response.status_code, 201)

    @patch('src.web.django_views.PedidoView.PedidoRepositoryOrm')
    def test_adicionar_pedido_sem_autenticacao_erro(self, mock_pedido_repository):
        mock_pedido_repository.addPedidoFromDict.side_effect = Exception('erro')
        client = Client()
        response = client.post('/pedido/', data=self.dicionario_pedido, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    @patch('src.web.django_views.PedidoView.PedidoRepositoryOrm')
    @patch('src.web.django_views.PedidoView.CognitoValidate')
    def test_adicionar_pedido_com_autenticacao(self, mock_cognito_validate, mock_pedido_repository):
        mock_pedido_repository.addPedidoFromDict.return_value = PedidoFactory.fromDict(self.dicionario_pedido)
        mock_cognito_validate = Mock()
        client = Client()
        response = client.post('/pedido/', data=self.dicionario_pedido, content_type='application/json',
                               headers={'Authorization': "Bearer dsadsadsadsadsa"})
        self.assertEqual(response.status_code, 201)
