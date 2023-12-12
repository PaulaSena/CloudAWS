Algoritmo "CriancaEsperanca"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : GustavoGuanabara
// Descrição   : CriancaEsperanca
// Autor(a)    : Ana Paula S Sena
// Data atual  : 11/12/2023
Var
   // Seção de Declarações das variáveis
   D, Valor: Inteiro
Inicio
      Escreval()
      Escreval(" ---------------------------")
      Escreval("      CRIANÇA ESPERANÇA     ")
      Escreval(" ---------------------------")
      Escreval(" [1] Para doar R$10")
      Escreval(" [2] Para doar R$25")
      Escreval(" [3] Para doar R$50")
      Escreval(" [4] Para doar outro valor!")
      Escreval(" [5] Para cancelar!")
      Leia(D)
      Escreval(" ---------------------------")
      Escreval()
      Escolha D
              Caso 1
                   Valor <- 10
              Caso 2
                   Valor <- 25
              Caso 3
                   Valor <- 50
              Caso 4
                   Escreva(" Digite o Valor: ")
                   Leia(Valor)
                              enquanto (Valor <= 5) faca
                                       Escreval(" Valor deve ser maior do que R$5")
                                       Leia(Valor)
                              fimenquanto
              Caso 5
                   Valor <- 1
      FimEscolha

      Se (D > 5) ou (D < 1) entao
         Escreval(" Opção Invalida")
      senao
           Se (Valor = 1) entao
              Escreval(" Ok! Doação cancelada :(")
           senao
                Escreval(" VOCÊ DOOU R$", Valor)
                Escreval(" Muito Obrigado!!")
                Escreval(" ---------------------------")
           Fimse
      Fimse

Fimalgoritmo