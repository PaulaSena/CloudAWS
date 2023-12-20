	
print()
print("Funcao média")
	
def media_aluno(notal, nota2):
    media = (notal + nota2) / 2
    return media

resultados = media_aluno(10, 8) 
print(resultados)

print("----------------------------------------------------------------")
print("Funcao média 2")
print()

def aprovacao(nota0l, nota02,nota03):
    soma = (nota0l + nota02 +nota03) / 3
    if (nota0l >= 7):
        res = "Aprovado"
    else:
        res = "Reprovado"
    return res




