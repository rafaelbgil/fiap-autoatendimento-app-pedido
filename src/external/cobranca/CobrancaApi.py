import requests
from requests import Response
from os import environ
from src.entities.Pedido import Pedido


class CobrancaApi:
    def __init__(self):
        self.api_url = environ.get('COBRANCA_API_URL')

    def adicionar_cobranca(self, pedido: Pedido) -> Response:
        dados_cobranca = {
            "id_pedido": pedido.numero,
            "status": "aguardando_pagamento",
            "valor": pedido.valor,
            "fornecedor_meio_pagto": "auto"
        }
        print('pasou pela cobranca')
        return requests.post(url=f'{self.api_url}/cobranca/', json=dados_cobranca)
