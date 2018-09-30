from unittest import TestCase

from SecuenciaNumeros import SecuenciaNumeros


class TestSecuenciaNumeros(TestCase):
    def test_retornarlongitud(self):
        self.assertEqual(SecuenciaNumeros().retornarlongitud(''), 0, 'cadena vacia')
        self.assertEqual(SecuenciaNumeros().retornarlongitud('12.5'), 1, 'cadena de un elemento')
        self.assertEqual(SecuenciaNumeros().retornarlongitud('12,5'), 2, 'cadena de dos elementos')
        self.assertEqual(SecuenciaNumeros().retornarlongitud('12,5,4,2'), 4, 'cadena de n elementos igual ')
        self.assertNotEqual(SecuenciaNumeros().retornarlongitud('12,5,4,2'), 5, 'cadena de n elementos no igual')


    def test_minimo(self):
        self.assertEqual(SecuenciaNumeros().minimo(''), 'vacio', 'cadena vacia minimo')


    def test_secuencia(self):
        self.assertEqual(SecuenciaNumeros().secuencia(''), str(SecuenciaNumeros().retornarlongitud(''))+','+str(SecuenciaNumeros().minimo('')), 'cadena vacia resultados')
