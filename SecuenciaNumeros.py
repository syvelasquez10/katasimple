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
        elif ',' not in cadena:
            return int(cadena)
        elif cadena.count(',') == 1:
            cadena_numeros = cadena.split(',')

            if int(cadena_numeros[0]) < int(cadena_numeros[1]):
                return int(cadena_numeros[0])
            else:
                return int(cadena_numeros[1])
        return -1