# Listas

# Antes 
nota1=7,9
nota2=8
nota3=4

# Com lista
notas=[7.9,8,4] 

# Criando Listas
lista = [] # lista vazia
lista = list() # metodo lista vazia - Converte estrutura em lista
lista = [26,"ana",3.14159,False]
lista_de_lista = [10,[1,2,3]] # lista de lista

# Indexação  Slice  acessa elementos da lista
lista = [31,"Paula",3.141,True]

print() # PULAR LINHA

# Ordem da lista

print(lista[0]) # 31
print(lista[1]) # Paula
print(lista[2]) # 3.141
print(lista[3]) # True

print() # PULAR LINHA

# Últimos da lista.

print(lista[-1]) # Acessa o Ultimo elemento da lista no caso acima o True
print(lista[-2]) # Acessa o Penultimo elemento da lista no caso acima o 3.141
print(lista[-3]) # Acessa o Antepenultimo elemento da lista no caso acima o Paula

print() # PULAR LINHA

""" SLICES  ( FATI A MENTO )  Pegar um pedaço da lista """

lista = [10,2,30,8,50,60,70]
print(lista[0:3]) # Para pegar do indice 0 ao 3 ou seja [10,2,30]
print(lista[3:6]) # Para pegar do indice 3 ao 6 MENOS O ULTIMO ou seja [8,50,60]  
print(lista[3:7]) # Para pegar do indice 3 ao ULTIMO ou seja [8,50,60,70]  
print(lista[0:]) # Para pegar DO 0 EM DIANTE ((TODOS))

print() # PULAR LINHA

""" SLICES PARECE MUITO COM O RANGE """
print(lista[0:12:2]) # Para pegar DO 0 EM DIANTE ((TODOS)) - inicia no indice 0, vai até o indice 12 de 2 em 2.
print() # PULAR LINHA

# Iteração com FOR

numItem=0 # para mostrar os numeros de itens
Lista_Feira = ["Banana","Alface","Maça","Rabanete","Laranja","Limão"]
print("Minha Cesta da Feira")

for item in Lista_Feira:
    numItem += 1 # adiciona mais um item a lista
    print(f"{numItem} - {item}")
    
    # LEN - QUANTIDADE DE ELEMENTOS
    
print("Total de Itens: ", len(Lista_Feira))

print() # PULAR LINHA

# LEN QUANTIDADE COM FOR (por numero do Indice do array apartir no 0)
for i in range(len(Lista_Feira)):
    print(f"{i} - {Lista_Feira[i]}")
