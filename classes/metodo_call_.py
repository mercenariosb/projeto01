class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self,nome):
        print(nome, 'esta chamando,', self.phone)


calll = CallMe('2343245345')
calll('luiz otavio')