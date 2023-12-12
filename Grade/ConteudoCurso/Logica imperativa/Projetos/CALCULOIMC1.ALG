Algoritmo "CalculoIMC"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : GustavoGuanabara
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Ana Paula S Sena
// Data atual  : 11/12/2023
Var
   // Seção de Declarações das variáveis
   M, A, IMC : Real
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreva("Massa (KG): ")
   Leia(M)
   Escreva("Altura (M): ")
   Leia(A)
   IMC <-M /(A ^ 2)
   Escreval("IMC: ",IMC:5:2)
   Se(IMC>=18.5) e (IMC<25) entao
      Escreva("Parabens! Você esta no seu Peso ideal")
   Senao
      Escreva("Você não esta no peso ideal")
      FimSe

Fimalgoritmo