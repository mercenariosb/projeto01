from dataclasses import dataclass

@dataclass

class Pessoa:
    nome: str
    idade: int
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '. join(sobrenome) # para ter varios sobrenomes
    
    

    """ Criando a classes de uma forma simples usando decorator 

    usando um data classe de uma forma mais rapida e simples, ela ja vem com __rper__  gueter e seter
    """

    """ A classe de cima é igual esta classe abaixo, resumido.
    class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs =  f'(nome: {self.nome!r}, idade: {self.idade!r})'
        
        return f'{class_name}{attrs}'
    
    """


p1 =Pessoa(" Dhecica", 26, "veigas antonia")
print(p1)
print(p1.nome_completo)
