import string

def substitution_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                index = ord(char) - ord('A')
                encrypted_char = key[index].upper()
            else:
                index = ord(char) - ord('a')
                encrypted_char = key[index].lower()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Obter a chave do usuário
key = input("Digite 26 letras do alfabeto fora de ordem como chave: ") # Não pode repetir as letras

# Verificar se a chave é válida
key = key.upper()
if len(key) != 26 or not all(char.isalpha() for char in key) or len(set(key)) != 26:
    print("A chave deve ser uma sequência de 26 letras do alfabeto sem repetições.")
    exit()

# Obter a mensagem para criptografar do usuário
message = input('Digite o texto')

# Criptografar a mensagem usando a cifra de substituição
encrypted_message = substitution_cipher(message, key)

print("Mensagem criptografada:", encrypted_message)

# teste de chave "badcegfhijklonmpqsrtvuxzwy"  
def substitution_cipher_decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                index = key.upper().index(char)
                decrypted_char = string.ascii_uppercase[index]
            else:
                index = key.lower().index(char)
                decrypted_char = string.ascii_lowercase[index]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Obter a chave do usuário
key = input("Digite 26 letras do alfabeto fora de ordem como chave: ") # Não pode repetir as letras

# Verificar se a chave é válida
key = key.upper()
if len(key) != 26 or not all(char.isalpha() for char in key) or len(set(key)) != 26:
    print("A chave deve ser uma sequência de 26 letras do alfabeto sem repetições.")
    exit()

# Obter a mensagem criptografada do usuário
ciphertext = input('Digite o texto')

# Descriptografar a mensagem usando a cifra de substituição
decrypted_message = substitution_cipher_decrypt(ciphertext, key)

print("Mensagem descriptografada:", decrypted_message)
