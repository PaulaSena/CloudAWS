# Cisco Packet Tracer

Para o show da banda de Miguel, será necessário configurar uma rede de computadores. A comunicação entre os membros da equipe de produção, que estarão espalhados pelo teatro, é fundamental para manter todos informados e verificar se nada está fugindo do controle. O agente da banda decidiu modernizar a infraestrutura do show para melhorar essa comunicação. Para ajudá-los, você deve usar o Cisco Packet Tracer para criar uma topologia de rede estrela que permita a toda a equipe se comunicar facilmente.

#Passos:
## 1. Definir o cenário
- Imagine que cada membro da equipe possui um computador que precisa de uma conexão de rede para se comunicar com os outros membros da produção.

## 2. Montar a topologia
[X] Crie uma nova topologia no Cisco Packet Tracer; 
[X] Arraste um switch para o centro da área de trabalho; 
[X] Arraste quatro PCs e posicione-os ao redor do switch, representando cada membro da equipe de produção.

## 3. Conectar os dispositivos
[X] Conecte cada PC a uma porta diferente no switch usando cabos ethernet;
[X] Visualize os computadores da equipe de produção formando uma estrela ao redor do switch central.

## 4. Configurar os endereços IP
[X] Crie um senso de identidade para cada computador, atribuindo nomes e números de endereços IP;
[X] Configure os endereços IP para as interfaces dos PCs e do switch de acordo com a mesma sub-rede.

## 5. Testar a comunicação
[X] Para verificar se todos os computadores estão devidamente configurados, acesse um dos PCs da equipe, abra o prompt de comando e tente fazer um ping para o endereço IP do computador de outro membro da equipe.

Por fim, envie o arquivo do Cisco gerado, junto com um print da tela com a topologia e do comando ping executado para os outros três computadores.

![CiscoPacktTrace1](https://github.com/PaulaSena/CloudAWS/blob/main/Grade/ConteudoCurso/AWS/Desenvolvimento/D1/img/desenvolvimento1AWS.gif?raw=true)


# PINGS
'''cmd
Cisco Packet Tracer PC Command Line 1.0
C:\>ping 192.168.2.1

Pinging 192.168.2.1 with 32 bytes of data:

Reply from 192.168.2.1: bytes=32 time=5ms TTL=128
Reply from 192.168.2.1: bytes=32 time<1ms TTL=128
Reply from 192.168.2.1: bytes=32 time<1ms TTL=128
Reply from 192.168.2.1: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.2.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 5ms, Average = 1ms

C:\>ping 192.168.2.3

Pinging 192.168.2.3 with 32 bytes of data:

Reply from 192.168.2.3: bytes=32 time<1ms TTL=128
Reply from 192.168.2.3: bytes=32 time<1ms TTL=128
Reply from 192.168.2.3: bytes=32 time<1ms TTL=128
Reply from 192.168.2.3: bytes=32 time<1ms TTL=128

Ping statistics for 192.168.2.3:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

C:\>ping 192.168.2.2

Pinging 192.168.2.2 with 32 bytes of data:

Reply from 192.168.2.2: bytes=32 time<1ms TTL=128
Reply from 192.168.2.2: bytes=32 time<1ms TTL=128
Reply from 192.168.2.2: bytes=32 time<1ms TTL=128
Reply from 192.168.2.2: bytes=32 time=9ms TTL=128

Ping statistics for 192.168.2.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 9ms, Average = 2ms

C:\>ping 192.168.2.4

Pinging 192.168.2.4 with 32 bytes of data:

Reply from 192.168.2.4: bytes=32 time=7ms TTL=128
Reply from 192.168.2.4: bytes=32 time<1ms TTL=128
Reply from 192.168.2.4: bytes=32 time=2ms TTL=128
Reply from 192.168.2.4: bytes=32 time=6ms TTL=128

Ping statistics for 192.168.2.4:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 7ms, Average = 3ms
'''

# Mensagem enviada 
![CiscoPacktTrace2](https://github.com/PaulaSena/CloudAWS/blob/main/Grade/ConteudoCurso/AWS/Desenvolvimento/D1/img/mensagemEnviada.PNG?raw=true)


