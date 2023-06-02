import secrets  # modo seguro para gerar senhas
import string as s
from secrets import SystemRandom as sr

print(''.join(sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))

"""
    cria uma senha criptografada    
    
"""