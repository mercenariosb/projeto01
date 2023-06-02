import random
from flask import Flask, request, render_template

app = Flask(__name__)

# Lista de palavras secretas
palavras_secretas = ["gato", "cachorro",
                     "elefante", "leão", "tigre", "girafa", "zebra"]

# Jogo da forca


@app.route('/', methods=['GET', 'POST'])
def jogo_da_forca():
    global letras_erradas, letras_certas, tentativas

    # Inicializar variáveis
    palavra_secreta = random.choice(palavras_secretas).lower()
    letras_erradas = ''
    letras_certas = ''
    tentativas = 6
    palavra_atual = palavra_secreta

    if request.method == 'POST':
        letra = request.form['letra'].lower()

        # Verificar se a letra já foi escolhida
        if letra in letras_certas or letra in letras_erradas:
            return render_template('jogo_da_forca.html', palavra_atual=palavra_atual, letras_erradas=letras_erradas, letras_certas=letras_certas, tentativas=tentativas, mensagem="Você já escolheu essa letra. Tente outra.")

        # Verificar se a letra está na palavra secreta
        if letra in palavra_secreta:
            letras_certas += letra
        else:
            letras_erradas += letra
            tentativas -= 1

        # Exibir estado atual da palavra secreta
        palavra_atual = ''
        for letra in palavra_secreta:
            if letra in letras_certas:
                palavra_atual += letra
            else:
                palavra_atual += '_'

        # Verificar se o jogador ganhou o jogo
        if palavra_atual == palavra_secreta:
            mensagem = 'Parabéns! Você ganhou!'
        else:
            mensagem = ''

        # Verificar se o jogador perdeu o jogo
        if tentativas == 0:
            mensagem = 'Que pena! Você perdeu! A palavra secreta era ' + palavra_secreta

        return render_template('jogo_da_forca.html', palavra_atual=palavra_atual, letras_erradas=letras_erradas, letras_certas=letras_certas, tentativas=tentativas, mensagem=mensagem)

    else:
        # Exibir estado inicial do jogo
        palavra_atual = ''
        for letra in palavra_secreta:
            palavra_atual += '_'
        return render_template('jogo_da_forca.html', palavra_atual=palavra_atual, letras_erradas=letras_erradas, letras_certas=letras_certas, tentativas=tentativas, mensagem='')


@app.route('/adicionar_palavra', methods=['GET', 'POST'])
def adicionar_palavra():
    if request.method == 'POST':
        palavra = request.form['palavra'].lower()
        if palavra not in palavras_secretas:
            palavras_secretas.append(palavra)
            return "Palavra adicionada com sucesso!"
        else:
            return "Essa palavra já foi adicionada anteriormente."
    return render_template('adicionar_palavra.html')


if __name__ == '__main__':
    app.run(debug=True)
