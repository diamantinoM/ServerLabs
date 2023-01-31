import sys
import os
import re


# MAC_RE = '[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}'

MAC_RE = '([0-9A-F]{2}:){5}[0-9A-F]{2}'

if len(sys.argv) < 2:
    print("Utilização:", sys.argv[0], "[-r] <ipv4_addr1> [<ipv4_addr2>...]", 
          file=sys.stderr)
    sys.exit(1)

ips = sys.argv[1:]
refresh = False
for arg in ips:
    if arg == '-r':
        refresh = True
        ips.remove('-r')


for ip in ips:
    if refresh:
        retcode = os.system('ping -c 3 ' + ip + ' > /dev/null')
        if retcode != 0:
            print("Erro ao invocar ping.", file=sys.stderr)

    with os.popen('arp -n ' + ip) as pipe:
        match = re.search(MAC_RE, pipe.read(), re.IGNORECASE)
        if match:
            print(match.group(0))
        else:
            print("Erro ao obter endereço MAC para IP: " + ip, 
                  file=sys.stderr)