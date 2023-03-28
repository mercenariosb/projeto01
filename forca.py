from visual import visual_dict
import random

palavra = open("palavras.txt", encoding="utf8")  # crie um txt " palavras.txt", nele você adiciona as palavras( uma palavra por linha).
dicar = open("dicas.txt", encoding="utf8")       # crie um txt  "dicas.txt", nele você adiciona as dicas (uma dica por linha, respeitando a ordem do arquivo palavra).
palavras = palavra.read().upper().split("\n")
dicas = dicar.read().split("\n")


def escolher_palavra_secreta():
    return random.choice(palavras)


def escolher_dica(palavra_secreta):
    indice = palavras.index(palavra_secreta)  # pega o indice do arquivo palavras e procura a dica pelo indice no arquivo dica.
    return dicas[indice]


def jogar_forca():
    palavra_secreta = escolher_palavra_secreta()
    dica = escolher_dica(palavra_secreta)
    letras_palavra_secreta = set(palavra_secreta)
    palpites = set()
    acertos = set()
    tentativas = 7

    while len(letras_palavra_secreta) > 0 and tentativas > 0:
        print(F"A DICA É : \n ########## \n {dica} \n ############# \n ")
        painel = [letra if letra in acertos else "_" for letra in palavra_secreta]
        painel_completo = " ".join(painel)

        print(painel_completo)
        print(f"Tentativas: {tentativas}")

        if len(palpites) > 0:
            print(f"Letras já escolhidas: {' '.join(palpites)}")

        palpite = input("Escolha uma letra: ").upper()

        if palpite in palpites:
            print("Você já escolheu essa letra antes! Escolha outra!")
        elif palpite in letras_palavra_secreta:
            acertos.add(palpite)
            letras_palavra_secreta.remove(palpite)
        else:
            print(f"A palavra secreta não contém a letra {palpite}!")
            tentativas -= 1
            print(visual_dict[tentativas])  # crie um visual e numere cada parte dele, como tem 7 tentativas crie 7 visuais.

        palpites.add(palpite)

    if tentativas == 0:
        print(f"Você perdeu! A palavra secreta era: {palavra_secreta}!")
        jogar_forca()
    else:
        print(f"Parabéns! Você acertou a palavra secreta: {painel_completo}!")
        jogar_forca()


jogar_forca()
    