print("----------------------------------------------------------------")
print("Funcao média 2")
print()

def aprovacao(nota0l, nota02,nota03):
    soma = (nota0l + nota02 + nota03) / 3
    if (nota0l >= 7):
        res = "Aprovado"
    else:
        res = "Reprovado"
    return res

aprovacao()