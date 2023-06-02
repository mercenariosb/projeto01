class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('olha o erro')
    raise exception_

try:
    levantar()

except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OutroError('outro erro')
    
    raise exception_ from error