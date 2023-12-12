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
   Escreval("Ao digitar o peso e altura digite utilizando o ponto. ")
   Escreval("Exemplo: Massa(Kg):70.00 Altura(m):1.60 ")
   Escreval("--------------")
   Escreva("Digite sua massa (Kg): ")
   Leia(M)

   Escreva("Digite sua altura (m): ")
   Leia(A)

   IMC <- M / (A ^ 2)

   Escreva("Seu IMC é: ", IMC:5:2)

   Se (IMC <= 17) Entao
      Escreval("Muito abaixo do Peso")
   Senao Se (IMC < 18.5) Entao
      Escreval("Abaixo do Peso")
   Senao Se (IMC < 25) Entao
      Escreval("Parabéns! Você está no seu Peso ideal")
   Senao Se (IMC < 30) Entao
      Escreval("Sobrepeso")
   Senao Se (IMC < 35) Entao
      Escreval("Obesidade")
   Senao Se (IMC < 40) Entao
      Escreval("Obesidade Mórbida")
   FimSe

Fimalgoritmo