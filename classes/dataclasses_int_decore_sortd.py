
from dataclasses import dataclass


@dataclass # (init=False " desativa init, frozen= True") frozen é uma boa pratica
class Pessoa: 
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'
    
    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '. join(sobrenome)


p1 = Pessoa('dhecica', 'veigas')
print(p1)
print(p1.nome_completo)
lista = [Pessoa('dhec', 'veigas'),Pessoa('dheci', 'deigas'),Pessoa('cica', 'leigas')]
ordenadas = sorted(lista, reverse=False, key=lambda p: p.nome) 
                            # pede para lambda ordenar por nome ou sobrenome
print(ordenadas)