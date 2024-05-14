import unittest
from src.entities.TypeCpf import Cpf


class TestTypeCpf(unittest.TestCase):
    def test_type_cpf_correto(self):
        cpf = Cpf(cpf='01234567890')
        self.assertEqual(cpf.__str__(), '01234567890')
        self.assertEqual(cpf.getCpfFormatado(), '012.345.678-90')

    def test_type_cpf_incorreto(self):
        self.assertRaisesRegexp(Exception, 'Cpf precisa ser string.', Cpf, 1)
        self.assertRaisesRegexp(Exception, 'Quantidade de números do cpf inválida.', Cpf, '012345679000')
