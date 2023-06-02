import random


r_range = random.randrange(10, 20)# caso coloque mais uma virgula pode especificar qual tipo de aleatoriedade quiser ex 2 para par 1 para impar
print(r_range)

r_range2 = random.randint(10, 20)


r_uniform = random.uniform(10, 20) # tem flaut e double

random.shuffle('randomiza uma variavel (lista)')

random.sample('lista', k='numero de dados') #choices repete valores da lista e choice pega so um valor fixo aleatorio

random.seed() # controla a aleatoriedade usando os segundos


