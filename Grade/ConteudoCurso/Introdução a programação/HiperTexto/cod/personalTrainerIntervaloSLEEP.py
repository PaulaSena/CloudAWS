

## Personal trainer
# João começou a se exercitar na academia e foi instruído por seu personal trainer a descansar exatamente por 45 segundos entre os exercícios, porém ele sempre excede esse tempo.

# Crie um programa que mostre o progresso desse intervalo em segundos e que avise sobre quando o tempo de descanso terminar.
import time

tempoInicial=1
tempoFinal=45

print("Iniciando descanso...")

for i in range(tempoInicial, tempoFinal + 1):
    print(i)
    time.sleep(1)
print("fim do descanso...")