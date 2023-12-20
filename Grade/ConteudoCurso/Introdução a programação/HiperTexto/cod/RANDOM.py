# Gerar Números Aleatórios:
#Use a função random() para gerar um número de ponto flutuante aleatório no intervalo [0.0, 1.0).
print("#### Gerar Números Aleatórios:")
import random
random_number = random.random()
print(random_number)

# Gerar Números Inteiros em um Intervalo:
# Use a função randint(a, b) para gerar um número inteiro aleatório no intervalo [a, b].
print("#### Gerar Números Inteiros em um Intervalo:")
random_integer = random.randint(1, 10)
print(random_integer)

# Gerar Números ponto flutuante:
# uniform(a, b): Retorna um número de ponto flutuante aleatório no intervalo [a, b).

print("Retorna um número de ponto flutuante aleatório no intervalo [a, b):")
numero_aleatorio = random.uniform(1.0, 5.0)

# Escolher um Elemento Aleatório de uma Sequência:
# Use a função choice(seq) para escolher um elemento aleatório de uma sequência.
print("#### Escolher um Elemento Aleatório de uma Sequência:")
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print(random_element)

# Embaralhar uma Sequência:
# Use a função shuffle(seq) para embaralhar aleatoriamente os elementos de uma sequência.
print("#### Embaralhar uma Sequência:")
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# Amostragem sem Substituição:
#Use a função sample(seq, k) para obter uma amostra aleatória de tamanho k de uma sequência sem substituição. 
print("#### Mostar sem Substituição (não repete o numero):")
my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list, 4)
print(random_sample)

# Amostragem com Substituição:
# Use a função choices(seq, k) para obter uma amostra aleatória de tamanho k de uma sequência com substituição.
print("#### Mostar com Substituição(pode repetir o numero):")
my_list = [1, 2, 3, 4, 5]
random_choices = random.choices(my_list, k=3)
print(random_choices)
