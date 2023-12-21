# Convertendo If para While

numero_sorteado = 15
numero_escolhido = int(input('Informe um número entre 1 a 20: '))

'''
if numero_escolhido !=numero_sorteado:
    print('Você não acertou')
else:
    print('Você acertou')
'''
    
    # Para evitar loop infinito verifique se a variavel, realmente muda de valor
while numero_escolhido != numero_sorteado:
    print('Você não acertou!!')
    numero_escolhido = int(input('Informe um número entre 1 a 20: ')) 
print('Você acertou', numero_escolhido+"!!")      

# Exemplo Extrutura com contador

contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1      # Para evitar loop infinito verifique se a variavel, realmente muda de valor
