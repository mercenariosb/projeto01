# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log') # Aqui foi bloqueado para não usar diretamente a classe log
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log): # Aqui é onde o usuario pode usar o codigo, ele herda log e os principios dele.
    def _log(self, msg):
        msg_formatada = f'{msg}({self.__class__.__name__})'
        print('Salvando no log:', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\r\n')
    
class LogPrintMixin(Log): # Aqui é onde o usuario pode usar o codigo, ele herda log e os principios dele.
    def _log(self, msg):
        print(f"{msg}({self.__class__.__name__})")

if __name__ == '__main__':    # Aqui foi bloqueado para poder ser usado apenas pelo Main

    lp = LogPrintMixin()

    lp.log_error('qualquer coisa')

    lp.log_success('que legal')

    lf = LogFileMixin()

    lf.log_error('qualquer coisa')

    lf.log_success('que legal')

