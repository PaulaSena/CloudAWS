import math

def soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")

def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"Resultado: {num1} x {num2} = {resultado}")

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número (não pode ser zero): "))
    if num2 == 0:
        print("Erro: Divisão por zero.")
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")

operacoes = True

def sair():
    if operacoes ==True and operacoes != 0:
        print("Saindo do programa.")
        operacoes = False
    else:
        operacoes = {
        '1': soma,
        '2': subtracao,
        '3': multiplicacao,
        '4': divisao,
        '0': sair
    }

def menu():
    while operacoes !=0:
        print("Escolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha in operacoes:
            operacoes[escolha]()
        else:
            print("Escolha inválida. Por favor, escolha uma operação válida.")


menu()
