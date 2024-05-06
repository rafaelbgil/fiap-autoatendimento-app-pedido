from src.usecases.interfaces.CatalogoWs import CatalogoWs
from uuid import UUID
from src.utils.validar_uuid import validar_uuid
from src.entities.Produto import Produto
from src.entities.ProdutoFactory import ProdutoFactory
from requests import get
from os import environ

class CatalogoWsImpl(CatalogoWs):
    @staticmethod
    def obter_produto_por_id(id: UUID | str) -> Produto:
        catalogo_url = environ.get('CATALOGO_API_URL')
        id_validado = validar_uuid(uuid=id)
        produto_response = get(f'{catalogo_url}/produto/{id_validado}/')
        if produto_response.status_code != 200:
                raise Exception(f'Nao foi possivel localizar o produto com codigo {id_validado}')
        return ProdutoFactory.fromDict(produto_response.json())