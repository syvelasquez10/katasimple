class SecuenciaNumeros:

    def secuencia(self,cadena):
        return str(self.retornarlongitud(cadena))+','+str(self.minimo(cadena))+','+str(self.maximo(cadena))

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

        else:
            cadena_numeros = cadena.split(',')
            min = int(cadena_numeros[0])
            for x in cadena_numeros:
                if int(x) < min:
                    min = int(x)

            return min

    def maximo(self, cadena):
        if cadena == '':
            return 'vacio'
        return -1