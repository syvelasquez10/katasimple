class SecuenciaNumeros:

    def secuencia(self,cadena):
        return str(self.retornarlongitud(cadena))+','+str(self.minimo(cadena))

    def retornarlongitud(self, cadena):
        if cadena == '':
            return 0
        else:
            cadena_numeros = cadena.split(',')
            return len(cadena_numeros)

    def minimo(self, cadena):
        if cadena == '':
            return 'vacio'
        return -1