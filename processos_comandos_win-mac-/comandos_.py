import subprocess
import sys

print(sys.platform) # ve o sistema operacional

cmd = ['ping', '127.0.0.1', '-c', '4'] # aqui voce pode mandar todos os comandos CMD

proc = subprocess.run( # texte codifica para texto os byts
    cmd, text=True
)
print(proc.args) # stderr ( ve erros) stdout ( ve a saida) return code ( diz se teve erros)

# caso  ostdout com capture output=True saia errado, acrecente o decode('cp850') na saida