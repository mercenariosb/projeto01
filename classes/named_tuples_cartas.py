

from collections import namedtuple
import random

Carta = namedtuple('Carta', ['valor', 'naipe'],
                   defaults= ["", ""])
nipes = {

    "nipe" : ['\u2660','\u2665', '\u2666', '\u2663' ],
    "valor" : ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # '\u2660': ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
    # '\u2665': ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
    # '\u2666': ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
    # '\u2663': ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
}
naipe_escolhido = random.choice(nipes["nipe"])
valor_escolhido = random.choice(nipes["valor"])
# naipe_escolhido = random.choice(list(nipes.values(1)))
# valor_escolhido = random.choice(list[naipe_escolhido])

Distribuindo_carta = Carta(valor_escolhido, naipe_escolhido)
print(Distribuindo_carta.valor, Distribuindo_carta.naipe)

# Distribuindo_carta = Carta(valor_escolhido, naipe_escolhido)
# print(Distribuindo_carta[0], Distribuindo_carta[1])


