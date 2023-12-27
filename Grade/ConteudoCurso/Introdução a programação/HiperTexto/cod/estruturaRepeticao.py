lojas = ["TheSof","Ellis D'aurelio", "Pedrinho SS", "SofiaBia"]



# Listas de pessoas aptas e Nessessidade especial
aptas = ["Marcia", "Graça", "Silvana", "Jucimara", "Fatima", "Ana Paula", "Mireli"]
enfermas = ["Dalva", "Tereza", "Urani", "Ildeni"]

# Grupos de 2 pessoas aptas e Nessessidade especial
grupos_aptas_enfermas = []
for a in aptas:
    for e in enfermas:
        grupos_aptas_enfermas.append((a, e))

# Grupos de 2 pessoas aptas e aptas
grupos_aptas_aptas = []
for i in range(len(aptas)):
    for j in range(i+1, len(aptas)):
        grupos_aptas_aptas.append((aptas[i], aptas[j]))

# Exibir os grupos formados
print("Grupos de 2 pessoas aptas e Nessessidade especial:")
for grupo in grupos_aptas_enfermas:
    print(f"({grupo[0]}, {grupo[1]})")

print("\nGrupos de 2 pessoas aptas e aptas:")
for grupo in grupos_aptas_aptas:
    print(f"({grupo[0]}, {grupo[1]})")



