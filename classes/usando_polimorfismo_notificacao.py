from abc import ABC, abstractmethod


class Notificacao:
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...  # cuidar assinatura no caso é bool, então todos tem que ser bool


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando: ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando: ', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    
    if notificacao_enviada:
        print("Notificacão enviada")
    
    else:
        print("notificação não enviada")

notificar(NotificacaoEmail('testando e-mail'))
notificar(NotificacaoSMS('testando SMS'))