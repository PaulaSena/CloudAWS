Algoritmo "Calculadora"
// Disciplina   : Lógica Imperativa
// Professor   : ---
// Descrição   : Exemplo de estrutura condicional múltipla escolha
// Autor(a)    : Ana Paula Sena da Silva
// Data atual  : 07/12/2023
Var
numero1,  numero2, resultado : Real
operacao : Caractere

Inicio
      escreva ("Digite o primeiro número: ")
      leia (numero1)
      escreva ("Digite o símbolo da operação: ")
      leia (operacao)
      escreva ("Digite o segundo número: ")
      leia (numero2)
escolha operacao
         caso "+"
            resultado <- numero1 + numero2
         caso "-"
            resultado <- numero1 - numero2
         caso "*"
            resultado <- numero1 * numero2
         caso "/"
            resultado <- numero1 / numero2
      fimescolha
      escreva ("Resultado: ", resultado)
      
      
      