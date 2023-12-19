
# FUNÇÃO RANGE ()

# ----- range(stop):

# imprimir os números de 0 a 4
print("#### imprimir os números de 0 a 4")
for i in range(5):
    print(i)

# imprimir os números Impares
print("#### imprimir os números Impares")

for i in range(1, 10, 2):
    print(i)

# imprimir os números par
print("#### imprimir os números par")

for i in range(0, 6, 2):
    print(i)


# Imprimir números de 2 a 7.
print("#### Imprimir os números de 2 a 7.")
for i in range(2, 8):
    print(i)

# Imprimir números de 0 a 10 de 2 em 2.
print("#### Imprimir números de 0 a 10 de 2 em 2.")
x = range (0,10,2)
for n in x :
    print(n)
    
# Imprimir números de 10 a 1.
print("#### Imprimir números de 10 até 1.")
x = range (10, 0, -1)
for n in x :
    print(n)
    
# imprimir uma lista com range
print("#### imprimir uma lista com range")
my_lista = list(range(5))
print(my_lista)