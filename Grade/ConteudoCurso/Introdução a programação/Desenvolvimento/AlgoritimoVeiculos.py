# Qual é a melhor categoria de habilitação para o veículo informado a partir das condições:

#Desenvolva um algoritmo que utilize as seguintes características de um veículo:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.


# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
# E: Veículos com quatro rodas ou mais e com mais de 6000 kg.


# Variaveis
qtdRodas=4
peso=6001
qtdPessoas=9

##  Perguntas para identificar a categoria da carta:
# O veículo é de quantas rodas?
# Qual o peso do veículo?
# Quantas pessoas o veículo comporta?

# Categoria A --> (Veículos com duas ou três rodas.)
if (qtdRodas ==2 or qtdRodas ==3 and qtdPessoas >=1 and qtdPessoas <=3  and peso <3500):
    print()
    print('Seu veículo é da Categoria A')
    print(f"Comporta {qtdPessoas} pessoas, possui {qtdRodas} rodas e seu peso é de {peso}")
    print("-------------------------------------------------------------------------------------")
    print()
    
#Categoria B --> (Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg.)
elif (qtdRodas ==4 and qtdPessoas <=8  and peso <=3500):
    print()
    print('Seu veículo é da Categoria B')
    print(f"Comporta {qtdPessoas} pessoas, possui {qtdRodas} rodas e seu peso é de {peso}")
    print("-------------------------------------------------------------------------------------")
    print()
    
#Categoria C --> (Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg.)
elif (qtdRodas >=4 and qtdPessoas <=8  and peso >=3500 and peso<=6000):
    print()
    print('Seu veículo é da Categoria C')
    print(f"Comporta {qtdPessoas} pessoas, possui {qtdRodas} rodas e seu peso é de {peso}")
    print("-------------------------------------------------------------------------------------")
    print()
    
#Categoria D  --> (Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas)
elif(qtdRodas >=4 and qtdPessoas >8 and peso >=3500 and peso<=6000):
    print()  
    print("================== CATEGORIA D =====================================================")
    print('Seu veículo é da Categoria D')
    print(f"Comporta {qtdPessoas} pessoas, possui {qtdRodas} rodas e seu peso é de {peso}")
    print("-------------------------------------------------------------------------------------")
    print() 

#Categoria E --> (Veículos com quatro rodas ou mais e com mais de 6000 kg).
elif(qtdRodas >=4 and qtdPessoas >8 and peso >6000):
    print()  
    print("================== CATEGORIA E =====================================================")
    print('Seu veículo é da Categoria E')
    print(f"Comporta {qtdPessoas} pessoas, possui {qtdRodas} rodas e seu peso é de {peso}")
    print("-------------------------------------------------------------------------------------")
    print() 
    
else:
    print()  
    print("=============== Atenção ========================================================================================")
    print(" Esse carro não se enquadra em nenhuma das Categorias de CNH, verifique os dados informados e tente novamente.")
    print("________________________________________________________________________________________________________________")
    print() 

