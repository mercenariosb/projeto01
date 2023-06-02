
class Caneta:

    def __init__(self, cor):
        self._cor = cor
        

    @property
    def cor(self):
       
        return self._cor
    
    @cor.setter
    def cor(self, valor):
       
        self._cor = valor
    

caneta = Caneta("azul")
caneta.cor = 'Rosa'

print(caneta.cor)