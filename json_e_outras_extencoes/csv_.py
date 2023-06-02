from pathlib import Path
import csv

caminho_csv = Path(__file__).parent / ' nome do arquivo'

with open(caminho_csv, 'r') as arquivo:
    leitor = csv.reader(arquivo)# se precisar de um dicionario pode usar dict reader
    next(leitor)

    print(next(leitor))

    for linha in leitor: # forma facil
        print(linha[]) # pode usar o indice das colunas
# para escrever dicionarios csv

""""
 caso tenha um dicionario ou uma lista de dicionario pode salvar em uma variavel e usar o codigo abaixo
"""

with open(caminho_csv, 'w') as arquivo:
    nome_coluna = # dicionariolista[indice].keys()
    escritor = csv.writer(arquivo) # para ler dicionario dictwriter (fieldnames=nome_coluna)
    #caso use o dicionario

    escritor.writerow(nome_coluna)# se for dicionario .writeheader

    for cliente in "dicionario":
        # print(cliente)
        escritor.writerow(cliente.values())
        