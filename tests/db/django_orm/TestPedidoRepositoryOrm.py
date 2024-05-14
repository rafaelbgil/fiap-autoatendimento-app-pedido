import unittest
from unittest.mock import Mock, patch

from src.db.django_orm.PedidoRepositoryOrm import PedidoRepositoryOrm
from src.entities.PedidoFactory import PedidoFactory
from src.entities.ItemPedidoFactory import ItemPedidoFactory
from src.entities.Pedido import Pedido
from api.models import Pedido as PedidoModel


class TestPedidoRepositoryOrm(unittest.TestCase):
    def setUp(self):
        self.lista_dicionario_item_pedido = [{
            "quantidade": 1,
            "nome": 'Coca Cola',
            "descricao": 'Refrigerante',
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

    @patch('src.db.django_orm.PedidoRepositoryOrm.PedidoModel')
    @patch('src.db.django_orm.PedidoRepositoryOrm.PedidoRepositoryOrm.pedidoOrmToPedido')
    def test_listar_pedidos(self, pedido_repository_mock, pedido_model_mock):
        pedido = PedidoFactory.fromDict(dicionario_pedido=self.dicionario_pedido)

        pedido_model_mock.objects.all.return_value = [1]
        pedido_repository_mock.return_value = pedido

        lista_pedidos = PedidoRepositoryOrm.listPedido()
        self.assertIsInstance(lista_pedidos, list)

    @patch('src.db.django_orm.PedidoRepositoryOrm.PedidoModel')
    def test_pedido_update_status(self, mock_pedido_model):
        pedido = PedidoFactory.fromDict(dicionario_pedido=self.dicionario_pedido)
        mock_get_pedido = Mock()
        mock_get_pedido.status = 'recebido'
        pedido_atualizado = PedidoRepositoryOrm.updateStatus(pedido=pedido, status='recebido')

        self.assertIsInstance(pedido_atualizado, Pedido)

    @patch('src.db.django_orm.PedidoRepositoryOrm.CobrancaModel')
    def test_update_by_webhook(self, mock_cobranca_model):
        mock_cobranca_model = Mock()
        dicionario_cobranca = {"status": "approved"}
        retorno = PedidoRepositoryOrm.updateStatusByWebhook('4ebf5daa-5758-4ab2-beab-2847d0a280b7',
                                                            dicionario_cobranca=dicionario_cobranca)
        self.assertTrue(retorno)

        dicionario_cobranca = {"status": "cancelled"}
        retorno = PedidoRepositoryOrm.updateStatusByWebhook('4ebf5daa-5758-4ab2-beab-2847d0a280b7',
                                                            dicionario_cobranca=dicionario_cobranca)
        self.assertTrue(retorno)

        dicionario_cobranca = {"status": "pending"}
        retorno = PedidoRepositoryOrm.updateStatusByWebhook('4ebf5daa-5758-4ab2-beab-2847d0a280b7',
                                                            dicionario_cobranca=dicionario_cobranca)
        self.assertTrue(retorno)
