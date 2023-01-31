"""
SÉRIE DE EXERCÍCIOS 2 

O objectivo deste exercício consiste em desenvolver um programa para 
obter endereços MAC (endereços nível 2) a partir de uma lista de 
endereços IPv4 passada a partir da linha de comandos. O programa deverá
ser invocado da seguinte forma:
 
$ python3 l2addr.py [-r] ipv4_addr1 [ipv4_addr2...]

De modo a garantir que o endereço IPv4 se encontra na cache ARP, é 
conveniente "pingar" primeiro o destino (mas limitando o número de 
pacotes ICMP a enviar). 
Para invocar os comandos ping e arp utilize a função popen (Process 
Open) do módulo os. Esta função invoca um programa lançando um 
processo e criando uma pipe entre a saída padrão do processo invocado 
e o processo invocador (que é o script em Python que estamos a 
desenvolver). Acedemos à pipe como a um ficheiro de texto, uma vez que 
os.popen devolve um file object, isto é, um objecto que representa um 
ficheiro de texto. 
Utilize o módulo re (regular expressions) para extrair os endereços de 
nível 2 através de uma expressão regular apropriada.

NOTA: Versão inacabada. Aceita apenas um IP na linha de comandos. 
Ignora a opção '-r'.
"""

import os
import re
import sys


MAC_RE = ('[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:'
          '[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}')

if len(sys.argv) < 2:
    print("Utilização: python3", sys.argv[0], "[-r] ipv4_addr1 [ipv4_addr2...]")
else:
    ip = sys.argv[1]
    pipe = os.popen('arp -n ' + ip)
    macs = re.findall(MAC_RE, pipe.read(), re.IGNORECASE)
    if len(macs) == 1:
        print(macs[0])
    else:
        print('Erro a invocar o comando ARP para o IP' + ip)
    pipe.close()

