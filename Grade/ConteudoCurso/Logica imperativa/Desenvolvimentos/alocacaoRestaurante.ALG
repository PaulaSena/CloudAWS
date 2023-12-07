Algoritmo "alocacaoRestaurante"
// Disciplina   : Lógica Imperial
// Professor   : ---
// Descrição   : Elabore um algoritmo que possa descobrir,
//    através de perguntas e respostas, em qual área de um restaurante
//    uma pessoa ou grupo de pessoas precisa ser alocada.
// Autor(a)    : Ana Paula Sena
// Data atual  : 07/12/2023


Var
    numeroDePessoas : Inteiro
    fumante, animaisEstimacao : Caractere
    
Inicio
  // Quantas Pessoas
 escreva("Quantas pessoas estão no grupo? ")
 leia(numeroDePessoas)

 // Se fumantes
 escreva("Alguma pessoa do grupo é fumante? (S para Sim, N para Não) ")
 leia(fumante)

 // Se animais de estimação
 escreva("Alguma pessoa do grupo tem animais de estimação? (S para Sim, N para Não) ")
 leia(animaisEstimacao)

 // Verifica a alocação com base nas respostas
    escolha
        // Caso seja um grupo de 5 ou mais pessoas
        caso numeroDePessoas >= 5
            escreva("Grupo grande! Será alocado no 1º andar.")
        // Caso haja fumantes ou animais de estimação
        caso fumante = "S" ou fumante = "s" ou animaisEstimacao = "S" ou animaisEstimacao = "s"
            escreva("Pessoas com necessidades especiais serão alocadas na área externa.")
        // Caso contrário, alocar no térreo
        caso contrario
            escreva("Grupo será alocado no térreo.")
    fimescolha
 
Fimalgoritmo