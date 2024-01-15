

def calculadora(num1, num2, operacao):
   
    operacoes = {
        '1': soma,
        '2': subtracao,
        '3': multiplicacao,
        '4': divisao,
        '0': sair
        }


    escolha = input("Digite o número da operação desejada: ")

    if escolha == 0:
        execultar=False  
    elif escolha in operacoes:
        operacoes[escolha]()
        print(escolha)
    else:
        print("Escolha inválida. Por favor, escolha uma operação válida.")

        


#print ( ""+ str(num1) + str(operador) + str(num2))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (0: Sair, 1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))



print("Bem vindo a Calculadora""\n")
print("Escolha uma operação:""\n")
print("1: Soma")
print("2: Subtração")
print("3: Multiplicação")
print("4: Divisão")
print("0: Sair ""\n")


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
def sair():
    executar=False


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


























    operacao_func = operacoes.get(operacao)
    if operacao_func:
        return operacao_func(num1, num2)
    else:
        return "Erro: Operação inválida."
    
    

resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)