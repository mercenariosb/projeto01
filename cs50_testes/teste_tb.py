def dividir_valor(valor):
    partes = []
    sobra = 0
    while valor >= 36:
        partes.append(36)
        valor -= 36
    sobra = valor
    partes.append(valor)
    return partes, sobra


dados = {}

while True:
    chave = input("Digite o lote (ou 'parar' para encerrar): ").lower()
    if chave == 'parar':
        break
    valor = int(input("Digite quantas bandejas: "))
    dados[chave] = valor

print()

sobra = 0
continuacao = 0
primeira_iteracao = True

chaves = list(dados.keys())
num_chaves = len(chaves)

indice_impressao = 1

for i, chave in enumerate(chaves):
    valor = dados[chave]
    proxima_chave = chaves[(i + 1) % num_chaves]
    partes, sobra = dividir_valor(valor + sobra - continuacao)
    continuacao = 36 - sobra

    if valor < 36:
        print(f"{indice_impressao}. {chave} = {valor}")
        indice_impressao += 1
        print(f"{proxima_chave} = {continuacao}")
        
        print()
        continue

    for i, parte in enumerate(partes):
        if parte == 36:
            print(f"{indice_impressao}. {chave} = {parte}")
            indice_impressao += 1
            if i < len(partes) - 1:
                print()

    if sobra != 0 and sobra != 36:
        print(f"{indice_impressao}. {chave} = {sobra}")
        indice_impressao += 1

    if continuacao != 0 or 0 and not primeira_iteracao:
        if continuacao - dados[proxima_chave] == 0:
            print(f" {proxima_chave} = {continuacao}")
            
            break

        print(f"{indice_impressao}. {proxima_chave} = {continuacao}")
        indice_impressao += 1
        print()

    primeira_iteracao = False
    sobra = 0

print()