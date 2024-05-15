Funcionalidade: Adicionar Pedido
    Cenário: Criacao de pedido pela api
        Dado que foram informados os dados para criacao do pedido
            '''
                {
                "id": 1,
                "cpf": "01234567890",
                "lista_itens": [
                    {
                      "quantidade": 1,
                      "nome": "Coca Cola",
                      "descricao": "Refrigerante",
                      "preco": 6.9,
                      "id_categoria": "4ebf5daa-5758-4ab2-beab-2847d0a280b7",
                      "imagem_url": "https://teste.com.br/refrigerante"
                    }
                ],
                "valor": 6.9,
                "status": "aguardando_pagamento"
                }
            '''
        E após a validação os dados estão corretos
        Quando a rotina de criação de pedido por executada
        Então será retornado o número os detalhes do pedido juntamente com o número