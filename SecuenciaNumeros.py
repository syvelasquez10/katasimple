class SecuenciaNumeros:

    def secuencia(self,cadena):
        return -1

    def retornarlongitud(self, cadena):
        if cadena == '':
            return 0
        else:
            cadena_numeros = cadena.split(',')
            return len(cadena_numeros)

    def minimo(self, cadena):
        return -1