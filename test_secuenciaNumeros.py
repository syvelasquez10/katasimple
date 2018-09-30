from unittest import TestCase

from SecuenciaNumeros import SecuenciaNumeros
class TestSecuenciaNumeros(TestCase):
    def test_retornarlongitud(self):
        self.assertEqual(SecuenciaNumeros().retornarlongitud(''), 0, 'cadena vacia')
        self.assertEqual(SecuenciaNumeros().retornarlongitud('107'), 1, 'cadena de un elemento')

