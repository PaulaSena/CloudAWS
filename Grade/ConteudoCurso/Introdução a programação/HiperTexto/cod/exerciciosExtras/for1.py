
'''
for i in range(5):
    print(i)
'''

'''
for variavel in range(5):
    print(variavel)
'''

'''
for variavel in range(5,11):
    print(variavel)
'''

''' 
for variavel in range(1,12,3):
    print(variavel)
'''
''' 
    nota1 = int(input("Insire uma nota:"))
    nota2 = int(input("Insire uma nota:"))
    nota3 = int(input("Insire uma nota:"))

    Para realizar o calculo de media e não precisar instanciar 
    varias variaveis como no exemplo acima podemos utilizaar o For

''' 

## Situação problema

'''
    Faça um programa que receba 3 notas usando o for    
'''
    
soma = 0  # contador
    
for i in range(1,4):   # iniciando em 1 a 3 notas range(1,4)
    nota = float(input(f"Informe a nota {i}: "))  # exibindo o numero de notas informados com f"{calculo_media}"     
    soma = soma + nota
    
print(soma/3)