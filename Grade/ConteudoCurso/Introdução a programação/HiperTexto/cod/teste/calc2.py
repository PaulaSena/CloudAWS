def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num1 == 0 or num2 == 0:
        return "Erro: Divisão por zero"
    else:
        return num1 / num2
calculadora = True
def calculadora():
    while True:
        print("Quais das operações abaixo deseja realizar:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        operacao = input("Digite o número da operação escolhida ou '0' para sair: ")
        print(" ")


        if operacao == '0':
            
            print("Saindo da calculadora.")
            calculadora = False
            break

        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))

        if operacao == '1': 
            operacao = '+'
            resultado = soma(num1, num2)
        elif operacao == '2':
            operacao = '-'
            resultado = subtracao(num1, num2)
        elif operacao == '3':
            operacao = '*'
            resultado = multiplicacao(num1, num2)
        elif operacao == '4':
            operacao = '/'
            resultado = divisao(num1, num2)
        else:
            print(" ")
            print("Essa opção não existe.")
            continue
        print(" ")

       #print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        print("Resultado " + str(num1) +" "+ str(operacao) +" "+ str(num2) + " = " + str(resultado))
              # Resultado: 5 + 5 = 10
        print(" ")


calculadora()
