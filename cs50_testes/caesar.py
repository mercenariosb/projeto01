import sys

def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Verificar se a chave foi fornecida como argumento de linha de comando
if len(sys.argv) != 2:
    print("Uso: python caesar.py <chave>")
    sys.exit(1)

# Obter a chave do argumento de linha de comando
try:
    key = int(sys.argv[1])
    if key < 0:
        raise ValueError
except (ValueError, IndexError):
    print("A chave deve ser um número inteiro positivo.")
    sys.exit(1)

# Obter a mensagem do usuário
message = input("Digite a mensagem a ser criptografada: ")

# Criptografar a mensagem usando a cifra de César
encrypted_message = caesar_cipher(message, key)

print("Mensagem criptografada:", encrypted_message)