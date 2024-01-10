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


# Importando a biblioteca para manipulação de datas
from datetime import datetime, timedelta

# Função para verificar se duas pessoas não podem estar juntas em uma sexta-feira
def is_invalid_friday_combination(person1, person2):
    invalid_combinations = [("Mireli", "Silvana"), ("Silvana", "Mireli")]
    return (person1, person2) in invalid_combinations or (person2, person1) in invalid_combinations

# Função para atribuir pessoas aos dias da semana
def assign_people_to_days(start_date, end_date, weekdays, people_combinations):
    current_date = start_date
    assignments = []

    while current_date <= end_date:
        weekday = current_date.strftime("%A")
        if weekday in weekdays:
            valid_combinations = [combo for combo in people_combinations if not is_invalid_friday_combination(combo[0], combo[1])]
            if valid_combinations:
                assignment = valid_combinations.pop(0)
                assignments.append((current_date.strftime("%B"), current_date.strftime("%d/%m/%Y"), weekday, assignment[0], assignment[1]))
            else:
                assignments.append((current_date.strftime("%B"), current_date.strftime("%d/%m/%Y"), weekday, "N/A", "N/A"))
        current_date += timedelta(days=1)

    return assignments

# Definindo o período desejado
start_date = datetime(2024, 4, 1)  # Próximo mês após a última data fornecida
end_date = datetime(2024, 12, 31)

# Definindo os dias da semana desejados
weekdays = ["Friday", "Sunday"]

# Criando a lista de combinações possíveis
people_combinations = [(a, e) for a in aptas for e in enfermas]

# Atribuindo pessoas aos dias da semana
assignments = assign_people_to_days(start_date, end_date, weekdays, people_combinations)

# Exibindo as atribuições
print("DATA\t\tCulto Oficial | R. Jovens | Ensaio")
for assignment in assignments:
    print(f"{assignment[1]}\t{assignment[2]}\t{assignment[3]}, {assignment[4]}")
