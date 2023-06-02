numero_andares = []


def piramide_tamanho():
    piramide = int(input('Tamanho da pirâmide: '))
    print(piramide)
    
    while piramide <= 1 or piramide == 0:
        print('A pirâmide precisa ter um tamanho maior que 1.')
        piramide = int(input('Tamanho da pirâmide: '))
    
    numero_andares.append(piramide)


piramide_tamanho()

for blocos in numero_andares:
    for i in range(1, blocos + 1):
        arterisco = '#' * i
        espaco = ' ' * (blocos - i)
        print(f'{espaco}{arterisco}')



