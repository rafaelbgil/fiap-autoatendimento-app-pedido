import unittest
from unittest.mock import Mock, patch
from src.external.catalogo.CatalogoWsImpl import CatalogoWsImpl
from src.entities.Produto import Produto

class TestCatalogoWsImpl(unittest.TestCase):
    @patch('src.external.catalogo.CatalogoWsImpl.get')
    def test_obter_produto_por_id(self, mock_get):
        dicionario_produto = {
            "id": '4ebf5daa-5758-4ab2-beab-2847d0a280b9',
            "nome": 'Coca Cola',
            "descricao": 'Refrigerante',
            "preco": 6.9,
            "id_categoria": "4ebf5daa-5758-4ab2-beab-2847d0a280b7",
            "imagem_url": 'https://teste.com.br/refrigerante'
        }
        mock_retorno_get = Mock()
        mock_retorno_get.status_code = 200
        mock_retorno_get.json.return_value = dicionario_produto
        mock_get.return_value = mock_retorno_get
        retorno_request = CatalogoWsImpl.obter_produto_por_id('4ebf5daa-5758-4ab2-beab-2847d0a280b9')

        self.assertIsInstance(retorno_request, Produto)
        self.assertEqual(retorno_request.descricao, 'Refrigerante')