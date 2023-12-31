import random

# Listas de pessoas aptas e Necessidade especial
aptas = ["Marcia", "Graça", "Silvana", "Jucimara", "Fatima", "Ana Paula", "Mireli", "Urani"]
necessidadeEspecial = ["Dalva", "Tereza", "Ildeni"]

# Grupos de 2 pessoas aptas e Necessidade especial
grupos_aptas_necessidadeEspecial = [(a, e) for a in aptas for e in necessidadeEspecial]

# Grupos de 2 pessoas aptas e aptas
grupos_aptas_aptas = [(i, j) for i in aptas for j in aptas]

# Embaralhar as listas
random.shuffle(grupos_aptas_necessidadeEspecial)
random.shuffle(grupos_aptas_aptas)

# Misturar as duas listas garantindo as especificações
lista_misturada = []

while grupos_aptas_necessidadeEspecial or grupos_aptas_aptas:
    if lista_misturada:
        # Se já houver elementos na lista misturada, garantir que a pessoa nova
        # apareça em uma linha até que todos os nomes tenham sido impressos
        while grupos_aptas_necessidadeEspecial and grupos_aptas_necessidadeEspecial[0][0] not in lista_misturada[-2:]:
            random.shuffle(grupos_aptas_necessidadeEspecial)
        while grupos_aptas_aptas and grupos_aptas_aptas[0][0] not in lista_misturada[-2:]:
            random.shuffle(grupos_aptas_aptas)
    
    # Adicionar o próximo grupo de 2 pessoas aptas e Necessidade especial
    if grupos_aptas_necessidadeEspecial:
        lista_misturada.extend(grupos_aptas_necessidadeEspecial.pop(0))

    # Adicionar o próximo grupo de 2 pessoas aptas e aptas
    if grupos_aptas_aptas:
        lista_misturada.extend(grupos_aptas_aptas.pop(0))

# Imprimir a lista misturada
print("\nLista Misturada:")
for i in range(0, len(lista_misturada), 2):
    print(f"{lista_misturada[i]}, {lista_misturada[i+1]}")
