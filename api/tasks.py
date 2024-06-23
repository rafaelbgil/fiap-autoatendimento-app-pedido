# Create your tasks here

from celery import shared_task
from api.models import Pedido
from src.usecases.UseCasePedido import UseCasePedido
from src.db.django_orm.PedidoRepositoryOrm import PedidoRepositoryOrm
from src.entities.PedidoFactory import PedidoFactory


@shared_task(queue='status_pagamento_pedido')
def atualizar_status_pagamento_queue(id_pedido: str, status: str):
    try:
        pedido = UseCasePedido.obterPedido(repositorio_pedido=PedidoRepositoryOrm, id=id_pedido)
        if status == 'recebido':
            UseCasePedido.atualizarStatusPedido(repositorio_pedido=PedidoRepositoryOrm, status='recebido',
                                                pedido=pedido)
        elif status == 'cancelado':
            UseCasePedido.atualizarStatusPedido(repositorio_pedido=PedidoRepositoryOrm, status='cancelado',
                                                pedido=pedido)
    except:
        print(f'Nao foi encontrado o pedido: {id_pedido}')
