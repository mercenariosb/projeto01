""" Este é um exemplo de documentação

Este modulo contem funcoes e exemplos de documentação de funÇões 
A função soma por exemplo.

"""

variavel_1 = 1

def soma(x: int | float, y: int | float) -> int | float:
    """
    Soma x e y

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float
    
    """
    return x + y

def Multiplica(
        x: int | float,
        y: int | float,
        z: int | float | None = None)-> \
              int | float:
    """Nultiplica x e y.
     
     Se z for enviado, multiplica x, y, z.    
    """
    
    if z is None:
        return x * y
    return x * y * z

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4