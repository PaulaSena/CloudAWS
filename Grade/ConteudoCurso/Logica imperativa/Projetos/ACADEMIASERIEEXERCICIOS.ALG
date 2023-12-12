Algoritmo "AcademiaSerieExercicios"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Proz Talento Cloud
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Ana Paula Sena Silva
// Data atual  : 11/12/2023
var
   nomeExercicio: caractere
   quantidadeRepeticoes, contador: inteiro

Inicio
   // Solicita o nome do exercício
   escreva("Digite o nome do exercício: ")
   leia(nomeExercicio)

   // Solicita a quantidade de repetições
   escreva("Digite a quantidade de vezes que deseja repetir o exercício: ")
   leia(quantidadeRepeticoes)

   // Repete a atividade a quantidade de vezes especificada
   para contador de 1 ate quantidadeRepeticoes faca
      escreval("Exercício ", contador, ": ", nomeExercicio)
   fimpara
FimAlgoritmo
