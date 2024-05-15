from behave import *
from unittest.mock import Mock
from json import loads
from src.entities.PedidoFactory import PedidoFactory
from src.entities.Pedido import Pedido

from src.usecases.UseCasePedido import UseCasePedido


@given(u'que foram informados os dados para criacao do pedido')
def step_impl(context):
    context.dicionario_pedido = loads(context.text)


@given(u'após a validação os dados estão corretos')
def step_impl(context):
    context.pedido = PedidoFactory.fromDict(context.dicionario_pedido)


@when(u'a rotina de criação de pedido por executada')
def step_impl(context):
    dicionario_pedido_retorno = context.dicionario_pedido
    dicionario_pedido_retorno['numero'] = 1

    mock = Mock()
    UseCasePedido = mock
    context.pedido_criado = UseCasePedido.criarPedidoFromDict.return_value = PedidoFactory.fromDict(
        dicionario_pedido=dicionario_pedido_retorno)


@then(u'será retornado o número e os detalhes do pedido')
def step_impl(context):
    assert (isinstance(context.pedido_criado, Pedido))

