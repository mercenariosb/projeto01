from typing import Any


def meu_repr(self):
    return f'{type(self).__name__({self.__dict__})}'

class Meta(type):  # Como o python cria uma class
    def __new__(msc, name, bases, dct):
        print("Meta class new")
        cls = super().__new__(msc, name, bases, dct)
        cls.attr = 1234
        cls.__repr__ = meu_repr

        if 'falar' not in cls.__dict__ or \
                not callable(cls.__dict__['falar']):
            raise NotImplementedError('implemente falar')
        return cls
    
    def __call__(self, *args, **kwargs):
        instancia =  super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('crie o atributo nome')
      
        return instancia


class Pessoa(object, metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu New')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome) -> None:
        print('meu Init')
        self.nome = nome

    def falar(self):
        print('falando...')

p1 = Pessoa('luiz')
p1.falar()