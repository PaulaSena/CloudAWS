def calculadoraImc(peso, altura):

     imc = peso/(altura*altura) * 10000

     if (imc <= 18.5): return "Magreza"
     elif (imc > 18.5) and (imc <= 24.9): return "Saudavel"
     elif (imc >= 25) and (imc <= 29.9): return "Sobrepeso"
     elif (imc > 30) and (imc <= 34.9): return "Obesidade grau 1"
     elif (imc > 35) and (imc <= 39.9): return "Obesidade severa grau 2"
     else : return "Obesidade morbida grau 3"

peso = 60
altura = 160
resultado = calculadoraImc(peso,altura)

print(resultado)