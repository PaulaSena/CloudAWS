# contagem de 0 a 10
i = 0
while (i < 10):
    print(i)
    i = i + 1
    
    
# WHILE DO

print("usanso o LOWER break")
#    while True:
        # Código a ser executado
#        resposta = input("Deseja continuar? (sim/não): ")

#        if resposta.lower() != 'sim':
#           break

print(" inicia em 10 e vai aumentando de 2 em 2 se == 14 continua e para no 20. breack ")   
numero =10
for i in range(10):
    numero = numero + 2
    if (numero == 14):
        continue
    if(numero == 20):
        break
    print(numero)   
    
    
print()
print("Exercício 1: Soma dos Números")
n = int(input("Digite um número: "))
soma = 0
print()
# Usando while
i = 1
while i <= n:
    soma += i
    i += 1
print(f"A soma dos números de 1 a {n} é: {soma}")
print()
# Usando for
soma = 0
for i in range(1, n + 1):
    soma += i
print(f"A soma dos números de 1 a {n} é: {soma}")
print()

# Verificar Números Primos
print()
print("Exercício 2: Verificar Números Primos")
numero = int(input("Digite um número: "))
primo = True

# Usando while
i = 2
while i <= numero // 2:
    if numero % i == 0:
        primo = False
        break
    i += 1
print(f"{numero} é {'primo' if primo else 'não primo'}.")
print()

# Usando for
primo = True
for i in range(2, numero // 2 + 1):
    if numero % i == 0:
        primo = False
        break
print(f"{numero} é {'primo' if primo else 'não primo'}.")

# Exercício 3: Manipulação de Listas
print()
print("Exercício 3: Manipulação de Listas")
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = []

# Usando while
i = 0
while i < len(lista_numeros):
    if lista_numeros[i] % 2 == 0:
        lista_pares.append(lista_numeros[i])
    i += 1
print("Lista de números pares:", lista_pares)
print()
# Usando for
for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
print("Lista de números pares:", lista_pares)
