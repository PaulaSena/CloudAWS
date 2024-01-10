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
    for j in range(i + 1, len(aptas)):
        grupos_aptas_aptas.append((aptas[i], aptas[j]))

# Datas e grupos já definidos
datas_e_grupos = [
    ("05/01/2024", grupos_aptas_enfermas[0]),
    ("07/01/2024", grupos_aptas_aptas[0]),
    # ... Continue adicionando as datas e grupos correspondentes
]

# Exibir os grupos formados
for data, grupo in datas_e_grupos:
    print(f"{data}\t{grupo[0]}, {grupo[1]}")
