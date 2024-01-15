from datetime import datetime, timedelta


from itertools import permutations

# Lista de meninos
participantes = ["Murilo", "Theo", "Miguel", "Guilherme"]

# Criar todas as permutações possíveis
permutacoes = list(permutations(participantes, 2))

# Embaralhar as permutações
import random
random.shuffle(permutacoes)

# Exibir os grupos misturados
print("\nGrupos misturados:")
for grupo in permutacoes:
    print(f"{grupo[0]}, {grupo[1]}")
