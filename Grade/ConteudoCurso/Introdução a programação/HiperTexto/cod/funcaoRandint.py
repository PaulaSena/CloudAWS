

### randint() random
 
# No exemplo, tem um código que mostrará na tela números aleatórios entre 1 e 10. Este comando será repetido até que o número aleatório seja 5. A função utilizada para gerar os números foi a randint().
print("No exemplo, tem um código que mostrará na tela números aleatórios entre 1 e 10. Este comando será repetido até que o número aleatório seja 5. A função utilizada para gerar os números foi a randint().")
import random
numero1 = random.randint(1,10)
while (numero1 !=5):
    print(numero1)
    numero1 = random.randint(1,10)
print()
# RandInt usando o For
print('  ((((((  RANDINT USANDO O FOR  ))))))')
### Esses exemplos utilizam a função randint() para gerar números inteiros aleatórios em intervalos específicos. 
# O _ é uma convenção em Python para indicar que a variável não será usada dentro do loop.
# Imprimir 5 números inteiros aleatórios entre 1 e 10 .
print("#### Imprimir 5 números inteiros aleatórios entre 1 e 10")
for _ in range(5):
    print(random.randint(1, 10))
print()
# Imprimir 10 números pares aleatórios entre 0 e 100.
print("  #### Imprimir 10 números pares aleatórios entre 0 e 100.")
for _ in range(10):
    print(random.randint(0, 50) * 2)
print()
# Imprimir 5 números ímpares aleatórios entre 1 e 20.
print("  #### Imprimir 5 números ímpares aleatórios entre 1 e 20.")
for _ in range(5):
    print(random.randint(1, 10) * 2 - 1)
print()
# RandInt usando o While
print('  ((((((  RANDINT USANDO O WHILE ))))))')
# Imprimir 5 números inteiros aleatórios entre 1 e 10 usando while.
print("  #### Imprimir 5 números inteiros aleatórios entre 1 e 10  usando while.")
contador = 0
while contador < 5:
    print(random.randint(1, 10))
    contador += 1
print()
# Imprimir 10 números pares aleatórios entre 0 e 100 usando while.
print("  #### Imprimir 10 números pares aleatórios entre 0 e 100 usando while.")
contador = 0
while contador < 10:
    print(random.randint(0, 50) * 2)
    contador += 1
print()
# Imprimir 5 números ímpares aleatórios entre 1 e 20 usando while.
print("  #### Imprimir 5 números ímpares aleatórios entre 1 e 20 usando while.")
contador = 0
while contador < 5:
    print(random.randint(1, 10) * 2 - 1)
    contador += 1
print()
# RandInt usando LISTAS
print(' [[[[[ RANDINT USANDO LISTAS ]]]]] ')
print()
# Criar uma lista com 5 números inteiros aleatórios entre 1 e 10.
print("  #### Criar uma lista com 5 números inteiros aleatórios entre 1 e 10")
lista1 = [random.randint(1, 10) for _ in range(5)]
print(lista1)
print()
# Criar uma lista com 10 números pares aleatórios entre 0 e 100.
print("  #### Criar uma lista com 10 números pares aleatórios entre 0 e 100.")
lista2 = [random.randint(0, 50) * 2 for _ in range(10)]
print(lista2)
print()
# Criar uma lista com 5 números ímpares aleatórios entre 1 e 20.
print("  #### Criar uma lista com 5 números ímpares aleatórios entre 1 e 20.")
lista3 = [random.randint(1, 10) * 2 - 1 for _ in range(5)]
print(lista3)
print()
print()
