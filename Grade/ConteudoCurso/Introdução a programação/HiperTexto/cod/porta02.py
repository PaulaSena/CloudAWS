import random

# Listas de pessoas aptas e Nessessidade especial
aptas = ["Marcia", "Graça", "Silvana", "Jucimara", "Fatima", "Ana Paula", "Mireli", "Urani"]
necessidadeEspecial = ["Dalva", "Tereza", "Ildeni"]

# Grupos de 2 pessoas aptas e Nessessidade especial
grupos_aptas_necessidadeEspecial = []
for a in aptas:
    for e in necessidadeEspecial:
        grupos_aptas_necessidadeEspecial.append((a, e))

# Grupos de 2 pessoas aptas e aptas
grupos_aptas_aptas = []
for i in aptas:
    for j in aptas:
        grupos_aptas_aptas.append((i, j))

# Exibir os grupos formados
print("Grupos de 2 pessoas aptas e Nessessidade especial:")
for grupo in grupos_aptas_necessidadeEspecial:
    print(f"{grupo[0]}, {grupo[1]}")

print("\nGrupos de 2 pessoas aptas e aptas:")
for grupo in grupos_aptas_aptas:
    print(f"{grupo[0]}, {grupo[1]}")

# Embaralhar as listas
random.shuffle(grupos_aptas_necessidadeEspecial)
random.shuffle(grupos_aptas_aptas)

# Misturar os grupos
grupos_misturados = []
while grupos_aptas_necessidadeEspecial or grupos_aptas_aptas:
    if grupos_aptas_necessidadeEspecial:
        grupos_misturados.append(grupos_aptas_necessidadeEspecial.pop())
    if grupos_aptas_aptas:
        grupos_misturados.append(grupos_aptas_aptas.pop())

# Exibir os grupos misturados
print("\nGrupos misturados:")
for grupo in grupos_misturados:
    print(f"{grupo[0]}, {grupo[1]}")
