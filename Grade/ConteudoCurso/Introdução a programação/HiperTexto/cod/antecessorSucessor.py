print()
print("Funcao pega o valor passado no parâmetro  e retorna seus números antecessor e sucessor")
	
def ant_e_suc(num):
  ant = num - 1
  suc = num + 1
  return ant, suc
 
antecessor, sucessor = ant_e_suc(5)
print(antecessor)
print(sucessor)