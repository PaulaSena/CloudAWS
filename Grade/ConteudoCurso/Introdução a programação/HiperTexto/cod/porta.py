# Listas de pessoas aptas e Necessidade especial
aptas = ["Marcia", "Graça", "Silvana", "Jucimara", "Fatima", "Ana Paula", "Mireli"]
enfermas = ["Dalva", "Tereza", "Urani", "Ildeni"]

# Grupos de 2 pessoas aptas e Necessidade especial
grupos_aptas_enfermas = [(a, e) for a in aptas for e in enfermas]

# Grupos de 2 pessoas aptas e aptas
grupos_aptas_aptas = [(aptas[i], aptas[j]) for i in range(len(aptas)) for j in range(i+1, len(aptas))]

# Exibir os grupos formados
print("Grupos de 2 pessoas aptas e Necessidade especial:")
for grupo in grupos_aptas_enfermas:
    print(f"({grupo[0]}, {grupo[1]})")

print("\nGrupos de 2 pessoas aptas e aptas:")
for grupo in grupos_aptas_aptas:
    print(f"({grupo[0]}, {grupo[1]})")


# Importando a biblioteca para manipulação de datas
from datetime import datetime, timedelta

# Função para atribuir pessoas aos dias da semana
def assign_people_to_days(start_date, end_date, weekdays, people_combinations):
    current_date = start_date
    assignments = []

    while current_date <= end_date:
        weekday = current_date.strftime("%A")
        if weekday in weekdays:
            valid_combinations = people_combinations
            if valid_combinations:
                assignment = valid_combinations.pop(0)
                assignments.append((current_date.strftime("%B"), current_date.strftime("%d/%m/%Y"), weekday, assignment[0], assignment[1]))
            else:
                assignments.append((current_date.strftime("%B"), current_date.strftime("%d/%m/%Y"), weekday, "N/A", "N/A"))
        current_date += timedelta(days=1)

    return assignments

# Definindo o período desejado até dezembro
start_date = datetime(2024, 4, 1)  # Próximo mês após a última data fornecida
end_date = datetime(2024, 12, 31)

# Definindo os dias da semana desejados
weekdays = ["Friday", "Sunday"]

# Criando a lista de combinações possíveis
people_combinations = [(a, e) for a in aptas for e in enfermas]

# Atribuindo pessoas aos dias da semana
assignments = assign_people_to_days(start_date, end_date, weekdays, people_combinations)

# Continuando a atribuição de pessoas aos dias da semana até o final do ano
while current_date.year == 2024:
    weekday = current_date.strftime("%A")
    if weekday in weekdays:
        valid_combinations = people_combinations
        if valid_combinations:
            assignment = valid_combinations.pop(0)
            assignments.append((current_date.strftime("%B"), current_date.strftime("%d/%m/%Y"), weekday, assignment[0], assignment[1]))
        else:
            assignments.append((current_date.strftime("%B"), current_date.strftime("%d/%m/%Y"), weekday, "N/A", "N/A"))
    current_date += timedelta(days=1)

# Exibindo as atribuições
print("\nDATA\t\tCulto Oficial | R. Jovens | Ensaio")
for assignment in assignments:
    print(f"{assignment[1]}\t{assignment[2]}\t{assignment[3]}, {assignment[4]}")
