from unittest import TestCase

from SecuenciaNumeros import SecuenciaNumeros


class TestSecuenciaNumeros(TestCase):
    def test_retornarlongitud(self):
        self.assertEqual(SecuenciaNumeros().retornarlongitud(''), 0, 'cadena vacia')
        self.assertEqual(SecuenciaNumeros().retornarlongitud('12.5'), 1, 'cadena de un elemento')
        self.assertEqual(SecuenciaNumeros().retornarlongitud('12,5'), 2, 'cadena de dos elementos')
        self.assertEqual(SecuenciaNumeros().retornarlongitud('12,5,4,2'), 4, 'cadena de n elementos igual')
        self.assertNotEqual(SecuenciaNumeros().retornarlongitud('12,5,4,2'), 5, 'cadena de n elementos no igual')


    def test_minimo(self):
        self.assertEqual(SecuenciaNumeros().minimo(''), 'vacio', 'cadena vacia minimo')
        self.assertEqual(SecuenciaNumeros().minimo('12'), 12, 'cadena de un elemento minimo')
        self.assertEqual(SecuenciaNumeros().minimo('12,8'), 8, 'cadena de dos elementos minimo')
        self.assertEqual(SecuenciaNumeros().minimo('12,5,4,2'), 2, 'cadena de n elementos igual minimo')
        self.assertNotEqual(SecuenciaNumeros().minimo('12,5,4,2'), 5, 'cadena de n elementos no igual minmo')

    def test_secuencia(self):
        self.assertEqual(SecuenciaNumeros().secuencia(''), str(SecuenciaNumeros().retornarlongitud(''))+','+str(SecuenciaNumeros().minimo(''))+','+str(SecuenciaNumeros().maximo(''))+','+str(SecuenciaNumeros().promedio('')), 'cadena vacia resultados')

    def test_maximo(self):
        self.assertEqual(SecuenciaNumeros().maximo(''), 'vacio', 'cadena vacia maximo')
        self.assertEqual(SecuenciaNumeros().maximo('12'), 12, 'cadena de un elemento maximo')
        self.assertEqual(SecuenciaNumeros().maximo('12, 5'), 12, 'cadena de dos elemento maximo')
        self.assertEqual(SecuenciaNumeros().maximo('1, 5, 6, 9'), 9, 'cadena de n elementos maximo')

    def test_promedio(self):
        self.assertEqual(SecuenciaNumeros().promedio(''), 'vacio', 'cadena vacia promedio')
        self.assertEqual(SecuenciaNumeros().promedio('12'), 12, 'cadena de un elemento promedio')