
"""
    programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
    o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

    Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
    o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

"""

def quantosAninhos():
    nome = input("Nome: ")
    
    while True:
        try:
            ano_nascimento = int(input("Ano de Nascimento (entre 1922 e 2021): "))
            if ano_nascimento < 1922 or ano_nascimento > 2021:
                print("Por favor, insira um ano de nascimento válido entre 1922 e 2021.")
                continue
            break
        except ValueError:
            print("Por favor, insira um valor numérico para o ano de nascimento.")
    
    idade = 2021 - ano_nascimento
    print(f"Olá, {nome}! Você tem {idade} aninhos.")

quantosAninhos()
