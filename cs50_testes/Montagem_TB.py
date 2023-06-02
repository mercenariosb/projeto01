def dividir_valor(valor):
    partes = []
    sobra = 0  # Variável para armazenar o valor que sobra
    while valor >= 36:
        partes.append(36)
        valor -= 36
    sobra = valor  # Armazena o valor que sobra
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

chaves = list(dados.keys())  # Obtém a lista de chaves
num_chaves = len(chaves)  # Obtém o número de chaves

for i, chave in enumerate(chaves):
    valor = dados[chave]
    proxima_chave = chaves[(i + 1) % num_chaves]# Obtém a próxima chave circularmente
    partes, sobra = dividir_valor(valor + sobra - continuacao)  # Adiciona a sobra e subtrai a continuação
    continuacao = 36 - sobra  # Calcula a continuação para a próxima chave

    if valor < 36:
        print(f"{chave} = {valor} ")
        
        print(f"{proxima_chave} = {continuacao}")
        print()
        continue
    
    for i, parte in enumerate(partes):
        if parte == 36:  # Verifica se a parte atual é igual a 36
            print(f"{chave} = {parte}")

            if i < len(partes) - 1:
                print()

    # Imprime a sobra, se for diferente de 0 e diferente de 36
    if sobra != 0 and sobra <= 36:
        print(f"{chave} = {sobra}")
       
    # Imprime o valor de continuação, se for diferente de 0 e não for a primeira iteração
        if continuacao != 0 or 0 and not primeira_iteracao:
        # Verifica se a continuação - valor da próxima chave é igual a 0 e para o loop
            if continuacao - dados[proxima_chave] == 0:
                print(f"{proxima_chave} = {continuacao}")
                break

            print(f"{proxima_chave} = {continuacao}")
            print()

        primeira_iteracao = False

        sobra = 0  # Reinicia a sobra para a próxima chave

print()
