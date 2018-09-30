class SecuenciaNumeros:

    def retornarlongitud(self, cadena):
        if cadena == '':
            return 0
        elif ',' not in cadena:
            return 1
        elif cadena.count(',') == 1:
            return 2
        return -1