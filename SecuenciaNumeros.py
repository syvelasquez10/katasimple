class SecuenciaNumeros:

    def retornarlongitud(self, cadena):
        if cadena == '':
            return 0
        elif ',' not in cadena:
            return 1
        return -1