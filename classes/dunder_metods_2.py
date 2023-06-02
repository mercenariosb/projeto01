class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'  # para quem quer um STR

    def __repr__(self):
        class_name = type(self).__name__
        # para desenvolvedores.
        return f'{class_name}(x= {self.x!r}, y={self.y!r})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self,other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return  resultado_self > resultado_other

if __name__ == '__main__' :
    p1 = Ponto(1, 2)  # 3
    p2 = Ponto(4, 5)  # 9
    p3 = p1 + p2

print(p1)
print(repr(p2))
print(p3)
print('P1 é maior que p2?  ', p1 > p2)

#ENSINANDO COMO SOMAR FUNCIONA NO PHYTON