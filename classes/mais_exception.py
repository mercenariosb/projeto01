
from contextlib import contextmanager

@contextmanager
def My_open(caminho_arquivo, modo):
    try:

        print('abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    # except Exception as e:
    #     print('ocorreu um erro')
       
    finally:
        print('Fechando arquivo')
        arquivo.close()
    
instancia = My_open('mais_excepion.txt', 'w')

with instancia as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)  # tem um erro
    arquivo.write('Linha 3\n')
    print('witch', arquivo)
