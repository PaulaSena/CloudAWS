# -*- coding: utf-8 -*-
"""Desenvolvimento_Atividade_Andar

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JBqZ1OCZAQdhq7oDYbFkkk-BnT1zvNY3

Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

Em While
"""

# while
print("Usando o While")

andar = 20
while andar >= 1:
    if andar == 13:
        andar -= 1
        continue
    print(andar)
    andar -= 1

"""Em For"""

# FOR
print("Usando o For")

for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)