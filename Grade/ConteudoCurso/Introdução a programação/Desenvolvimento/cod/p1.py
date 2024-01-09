from itertools import permutations

# Lista de nomes
nomes = ["Murilo", "Theo", "Miguel", "Guilherme"]

# Gere todas as permutações possíveis
todas_permutacoes = list(permutations(nomes, 2))

# Exiba as duplas
for dupla in todas_permutacoes:
    print(dupla)
