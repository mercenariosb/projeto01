
import enum

# direcoes = enum.Enum('direcoes', ['ESQUERDA', 'DIREITA'])
# print(direcoes(1))

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

def mover(direcao: Direcoes):

    if not isinstance(direcao, Direcoes):
        raise ValueError('direção não encontrada')
    print(f'movendo para{direcao}')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
