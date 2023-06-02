

class Multiplicar:
    def __init__(self, multiplicador) -> None:
        self._multiplicador = multiplicador
    
    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

        




@Multiplicar(2)
def soma( x , y):
    return x + y

dois_m = soma(2,2)
print(dois_m)