class SecuenciaNumeros:

    def retornarlongitud(self, cadena):
        if cadena == '':
            return 0
        else:
            cadena_numeros = cadena.split(',')
            return len(cadena_numeros)