from unittest.mock import Mock, patch
import unittest
from src.entities.CobrancaFactory import CobrancaFactory
from src.entities.Cobranca import Cobranca


class TestCobrancaFactory(unittest.TestCase):
    def test_criar_cobranca(self):
        cobranca = CobrancaFactory.createCobranca(valor=10, fornecedor_meio_pagto='mercadopago', status='pendente',
                                                  pix_codigo='sasasasasasa',
                                                  codigo='9f803097-750c-455a-b786-e68cac5deee0')
        self.assertIsInstance(cobranca, Cobranca)