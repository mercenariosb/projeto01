import contas
from banco import Banco
import pessoas



cliente_1 = pessoas.Cliente('Dhecica', 26)
Dhecica = cliente_1.conta = contas.ContaCorrente(111, 222, 0, 100)
    
banco = Banco()
banco.clientes.extend([cliente_1, Dhecica])
banco.contas.extend([cliente_1, Dhecica])
banco.agencias.extend([111, 222])



if banco.autenticacao(cliente_1, Dhecica):
    Dhecica.depositar(110)

    print(f'{cliente_1}{cliente_1.conta}{Dhecica.saldo}')

    Dhecica.sacar(250)

    Dhecica.depositar(100)

    print(f'{cliente_1}{cliente_1.conta}Saldo em conta: {Dhecica.saldo}')