

# class open ('caminho do arquivo', " w ") as arquivo:
#     ...

class MyOpen:

    def __init__(self, caminho_arquivo, modo) -> None:
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
        

    def __enter__(self):
        print('Abrindo o arquivo!')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
        # print('enter')   
        # return 1234  # isto se torna a variavez alguma_coisa

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando o arquivo')
        self._arquivo.close()

        print(class_exception)
        print(exception_)
        print(traceback_)
        
        return True # tratei a exceção Força o erro a Passar



instancia = MyOpen('duck_metodos.txt', 'w')
    
with instancia as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123) # tem um erro
    arquivo.write('Linha 3\n')
    print('witch', arquivo)