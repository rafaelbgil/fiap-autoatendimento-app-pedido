import unittest
from src.utils.validar_uuid import validar_uuid
from uuid import UUID


class TestUtilsPedido(unittest.TestCase):
    def test_validar_uuid_corretamente(self):
        self.assertIsInstance(validar_uuid('6a125f4f-7446-44aa-b452-db47d1cbce47'), UUID)

    def test_validar_uuid_none(self):
        self.assertIsNone(validar_uuid(None))

    def test_validar_uuid_correto_type_uuid(self):
        self.assertIsInstance(validar_uuid(UUID('6a125f4f-7446-44aa-b452-db47d1cbce47')), UUID)

    def test_validar_uuid_erro_formato(self):
        self.assertRaisesRegexp(AttributeError, 'Formato de uuid inválido.', validar_uuid, 'assa')

    def test_validar_uuid_erro_type_formato(self):
        self.assertRaisesRegexp(AttributeError, 'Formato de uuid inválido.', validar_uuid, 1)