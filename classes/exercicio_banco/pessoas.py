import contas

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
    

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == "__main__":
    c1 = Cliente('Luiz', 30)
    c1.conta = contas.ContaCorrente(111, 222, 333, 3333)
    print(c1)
    print(c1.conta)

    cp1 = Cliente('antonio', 25)
    cp1.conta = contas.ContaPoupanca(111, 222, 333)
    print(cp1)
    print(cp1.conta)