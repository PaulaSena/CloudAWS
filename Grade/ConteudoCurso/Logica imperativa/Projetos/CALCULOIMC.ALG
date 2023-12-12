Algoritmo "CalculoIMC"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : GustavoGuanabara
// Descrição   : CalculoIMC
// Autor(a)    : Ana Paula S Sena
// Data atual  : 08/12/2023
Var
   // Seção de Declarações das variáveis
   M, A, IMC : Real
Inicio
   Escreval()
   Escreval()
   Escreval(" Ao digitar o valor de PESO e ALTURA utilize o ponto (.) ")
   Escreval()
   Escreval("   Exemplo: ")
   Escreval(" Massa(Kg: 70.00")
   Escreval(" Altura(m): 1.60 ")
   Escreval()
   Escreval(" ----------------------------")
   Escreval("        CALCULO DO IMC      ")
   Escreval("  (Índice de Massa Corporal)")
   Escreval(" ----------------------------")
   Escreval()
   Escreva(" Digite sua Massa (Kg): ")
   Leia(M)
   Escreva(" Digite sua Altura (m): ")
   Leia(A)

   IMC <- M / (A ^ 2)

   Escreval(" IMC: ", IMC:5:2)

   se (IMC < 17) entao
      Escreva(" Muito abaixo do Peso!")
   senao
      se (IMC >= 17) e (IMC < 18.5) entao
         Escreva(" Abaixo do Peso!")
      senao
         se (IMC >= 18.5) e (IMC < 25) entao
            Escreva(" Parabéns esta no seu peso ideal!")
         senao
            se (IMC >= 25) e (IMC < 30) entao
               Escreva(" Acima do Peso")
            senao
               se (IMC >= 30) e (IMC < 35) entao
                  Escreva(" Obesidade I")
               senao
                  se (IMC >= 35) e (IMC < 40) entao
                     Escreva(" Obesidade II (Sevéra)")
                  senao
                     Escreva(" Obesidade III (Mórbida)")
                        Escreval()
                  fimse
               fimse
            fimse
         fimse
      fimse
   fimse

Fimalgoritmo