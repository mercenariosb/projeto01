import contas
import pessoas


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None
            ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
        
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print("_checa_agencia", True)
            return True
        print("_checa_agencia", False)
        return False
    
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print("_checa_cliente", True)
            return True
        print("_checa_cliente", False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print("_checa_conta", True)
            return True
        print("_checa_conta", False)
        return False
    
    def __checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print("__checa_se_conta_e_do_cliente", True)
            return True
        print("__checa_se_conta_e_do_cliente", False)
        return False

    def autenticacao(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self.__checa_se_conta_e_do_cliente(cliente, conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'(agencia: {self.agencias!r}, conta: {self.contas!r}, {self.clientes!r})'

        return f'{class_name}{attrs}'
        
if __name__ == "__main__":
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = c1.conta = contas.ContaCorrente(111, 222, 333, 3333)
    

    cp1 = pessoas.Cliente('antonio', 25)
    cp1.conta = contas.ContaPoupanca(111, 222, 333)
    
    banco = Banco()
    banco.clientes.extend([c1, cp1])
    banco.contas.extend([c1.conta, cp1.conta])
    banco.agencias.extend([111, 222])

    print(banco.autenticacao(c1, cc1))

    if banco.autenticacao(c1, cc1):
        cc1.depositar(10)
        print(f'{c1}{c1.conta}{cc1.saldo}')
        cc1.sacar(343)
        cc1.depositar(100)
        print(f'{c1}{c1.conta}{cc1.saldo}')
    