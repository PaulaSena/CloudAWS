Algoritmo "Contador0"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Proz Talento Cloud
// Descrição   : Neste exemplo, O número digitado pelo usuário é somado ao contador e essa soma é apresentada na tela. O contador para de somar quando o usuário digitar 0, encerrando a execução do algoritmo.
// Autor(a)    : Ana Paula Sena da Silva
// Data atual  : 11/12/2023
Var
   // Seção de Declarações das variáveis
   numero : inteiro
   contador : inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...

      contador <- 0
      REPITA
        Escreval()
          ESCREVA ("Digite um número para a somar:  ")
          LEIA (numero)
          contador <- contador + numero
          ESCREVAL ("Total: ", contador)
      ATE numero = 0

Fimalgoritmo