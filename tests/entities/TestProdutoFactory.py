import unittest
from unittest.mock import Mock, patch

from src.entities.ProdutoFactory import ProdutoFactory
from src.entities.Produto import Produto


class TestProdutoFactory(unittest.TestCase):
    def setUp(self):
        self.dicionario_produto = {
            "id": 1,
            "nome": 'Coca Cola',
            "descricao": 'Refrigerante',
            "preco": 6.9,
            "id_categoria": "4ebf5daa-5758-4ab2-beab-2847d0a280b7",
            "imagem_url": 'https://teste.com.br/refrigerante'
        }

    def test_criar_produto(self):
        produto = ProdutoFactory.fromDict(self.dicionario_produto)
        self.assertIsInstance(produto, Produto)
        self.assertEqual(produto.nome, 'Coca Cola')

    def test_criar_produto_erro_valor_formato(self):
        dicionario_produto = self.dicionario_produto
        dicionario_produto['preco'] = None
        self.assertRaises(Exception, 'Formato de preco inválido, utilize somente inteiros ou float.',
                          ProdutoFactory.fromDict, dicionario_produto)
