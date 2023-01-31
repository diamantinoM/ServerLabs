"""
SÉRIE DE EXERCÍCIOS 3 - Controlo da Execução

Defina um gerador para datas semelhante em "espírito" ao range. Ou seja, 
pode receber um, dois ou três argumentos. Se receber apenas um argumento,
gera todas as datas da data actual até essa data. Se receber dois 
argumentos, assume que esses argumentos são datas e gera todas as datas 
entre as datas passadas como argumento. O terceiro argumento, caso seja 
utilizado, é um número inteiro que indica o número de dias de intervalo 
entre as datas a gerar. Dê o nome `date_range` ao gerador.
"""

from datetime import datetime, date, timedelta


def date_range(first, last=None, step=None):
    """
    Returns a generator from first until last, stepping by the number
    of days given by step. Parameters first and last are both either
    datetimes or dates. Granularity is "daily", so two datetimes are
    the same if their calendar date is the same, regardless of hour,
    min, etc.
    You can go backwards in time, in which case first should be > last
    and step should be negative.
    If no value is passed to last, then the value in first is assumed
    to be the finishing date/time, and date_range generates dates from
    date.today() until that date.
    """

    # If last isn't passed, then first is last and we want to iterate 
    # from today until first/last.
    # We deviate from range function, in which we assume that if last
    # is less (ie, before) than today then we want to go backwards
    # and thus we need to set the step to 1
    if last is None:
        last = first
        first = date.today()        
        if step is None:
            step = 1 if first < last else -1

    if step is None:
        step = 1

    if step == 0:
        raise ValueError("Step must not be zero")

    timedelta_step = timedelta(days=step)

    # Ensure that first and last are dates, otherwise we might have
    # one extra day if first.time < last.time
    first = first.date() if isinstance(first, datetime) else first
    last  = last.date()  if isinstance(last, datetime) else last

    dif = (last - first).days
    curr  = first
    for i in range(0, dif, step):
        yield curr
        curr += timedelta_step        


def test():
    today = date.today()
    dtA = today - timedelta(days=10)
    dtB = today + timedelta(days=10)
    step = 1

    print("[+] From {} until {} by {} days(s).".format(today, dtB, step))
    for dt in date_range(dtB):
        print(dt)

    print("[+] From {} until {} by {} days(s).".format(today, dtB, 2*step))
    for dt in date_range(today, dtB, 2*step):
        print(dt)

    print("[+] From {} until {} by {} days(s).".format(dtA, dtB, step))
    for dt in date_range(dtA, dtB):
        print(dt)

    print("[+] From {} until {} by {} days(s).".format(today, dtA, -step))
    for dt in date_range(today, dtA, -step):
        print(dt)

if __name__ == '__main__':
    test()


