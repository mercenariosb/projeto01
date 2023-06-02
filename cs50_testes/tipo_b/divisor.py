class DivisorDeValor:
    def __init__(self):
        self.dados = {}
        self.sobra = 0
        self.continuacao = 0
        self.primeira_iteracao = True

    def dividir_valor(self, valor):
        partes = []
        sobra = 0
        while valor > 36:
            partes.append(36)
            valor -= 36
        sobra = valor
        partes.append(valor)
        return partes, sobra

    def adicionar_dado(self, chave, valor):
        self.dados[chave] = valor

    def executar(self):
        chaves = list(self.dados.keys())
        num_chaves = len(chaves)

        for i, chave in enumerate(chaves):
            valor = self.dados[chave]
            proxima_chave = chaves[(i + 1) % num_chaves]
            partes, sobra = self.dividir_valor(valor + self.sobra - self.continuacao)
            self.continuacao = 36 - sobra

            if valor < 36:
                print(f"{chave} = {valor}")
                print(f"{proxima_chave} = {self.continuacao}")
                print()
                continue

            for i, parte in enumerate(partes):
                if parte == 36:
                    print(f"{chave} = {parte}")
                    if i < len(partes) - 1:
                        print()

            if sobra != 0 and sobra != 36:
                print(f"{chave} = {sobra}")

            if self.continuacao != 0 and not self.primeira_iteracao:
                if self.continuacao - self.dados[proxima_chave] == 0:
                    print(f"{proxima_chave} = {self.continuacao}")
                    break

                print(f"{proxima_chave} = {self.continuacao}")
                print()

            self.primeira_iteracao = False
            self.sobra = 0


divisor = DivisorDeValor()

