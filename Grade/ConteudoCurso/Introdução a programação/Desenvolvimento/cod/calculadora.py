
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))


def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero."

def calculadora(num1, num2, operacao):
    operacoes = {
        1: soma,
        2: subtracao,
        3: multiplicacao,
        4: divisao
    }

    operacao_func = operacoes.get(operacao)
    if operacao_func:
        return operacao_func(num1, num2)
    else:
        return "Erro: Operação inválida."
    
    

resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)

