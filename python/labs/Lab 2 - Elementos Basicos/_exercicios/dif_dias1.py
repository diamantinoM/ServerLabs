# Investigue o módulo datetime e faça um programa que quando chamado 
# sem argumentos indica a data/hora actual. Alternativamente, pode 
# receber uma ou duas datas, indicando o número de dias entre estas 
# datas. Se apenas receber uma data, utiliza como segunda data a 
# data actual.

import sys
from datetime import datetime, date

if len(sys.argv) not in (1, 2, 3):
    print(f"Utilização: {sys.argv[0]} [DATA1 [DATA2]]", file=sys.stderr)
    print("               DATA1/2 = YYYY-MM-DD", file=sys.stderr)
    sys.exit(2)

if len(sys.argv) == 1:
    print(f"Data/hora actual: {datetime.now()}")
elif len(sys.argv) == 2:
    # dt1_str = sys.argv[1].split('-')
    # dt1 = date(int(dt1_str[0]), int(dt1_str[1]), int(dt1_str[2]))

    # dt1 = datetime.strptime(sys.argv[1], "%Y-%m-%d").date()

    dt1 = date.fromisoformat(sys.argv[1])

    dt2 = date.today()
    print(f"Dias entre {dt1} e {dt2}: {(dt2 - dt1).days}")
elif len(sys.argv) == 3:
    dt1 = date.fromisoformat(sys.argv[1])
    dt2 = date.fromisoformat(sys.argv[2])
    print(f"Dias entre {dt1} e {dt2}: {(dt2 - dt1).days}")


