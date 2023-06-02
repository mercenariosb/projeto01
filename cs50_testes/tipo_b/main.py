from divisor import divisor

while True:
    chave = input("Digite a chave (ou 'parar' para encerrar): ").lower()
    if chave == 'parar':
        break
    valor = int(input("Digite o valor: "))
    divisor.adicionar_dado(chave, valor)

print()

divisor.executar()