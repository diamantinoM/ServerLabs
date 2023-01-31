import datetime 
from typing import Union 

# EXERCÍCIO:

class Date:
    def __init__(self, year: int, month: int, day: int):
        # VALIDAÇÕES
        if year < 1900:
            raise ValueError(f'year should be >= 1900 and not {year}')

        if not 1 <= month <= 12:
            raise ValueError(f'invalid month {month}')

        valid_date_parts = (
                1 <= day <= 31 and month in (1, 3, 5, 7, 8, 10, 12)
            or  1 <= day <= 30 and month in (4, 6, 9, 11)
            or  1 <= day <= 29 and month == 2 and is_leap_year(year)
            or  1 <= day <= 28 and month == 2 and not is_leap_year(year)
        )
        if not valid_date_parts:
            raise ValueError(f'invalid day {day} for month {month}')

        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date: str):
        # datetime.datetime.strptime(date, "%Y-%m-%d")
        date_parts = date.split('-')
        return cls(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))

    def __str__(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.year}, {self.month}, {self.day})'

    @property
    def is_leap_year(self):
        return is_leap_year(self.year)

    def __add__(self, days: int):
        dt = datetime.date(self.year, self.month, self.day)
        dt2 = dt + datetime.timedelta(days=days)
        return Date(dt2.year, dt2.month, dt2.day)

    def __radd__(self, days: int):
        return self + days

    def __sub__(self, days_or_date: Union[int, 'Date']):
        dt = datetime.date(self.year, self.month, self.day)
        if isinstance(days_or_date, int):
            days = days_or_date
            dt2 = dt - datetime.timedelta(days=days)
            return Date(dt2.year, dt2.month, dt2.day)
        
        date2 = days_or_date
        dt2 = datetime.date(date2.year, date2.month, date2.day)
        return (dt - dt2).days

def is_leap_year(year: int):
    return year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)

dt1 = Date(2020, 2, 6)

# classe Date
#   + construtores:
#       o __init__ : ano, mes, dia, tem que ser validados (não aceitar 31/4,
#                    29/2/2019, ); lançar excepção do tipo InvalidDateValues que 
#                    deve derivar de ValueError
#       o construtor: data no formato AAAA-MM-DD
#       o construtor: data como inteiro (juliano) AAAAMMDD
#   + acessores:
#       o year, month, day (properties)
#   + predicados ("acessor" booleano):
#       o is_leap_year
#   + __str__ : mostra data 'AAAA-MM-DD'
#   + __repr__: mostra 'Date(ano, mês, dia)'
#   + outros métodos:
#       o __add__  : nova data igual a data + dias (int)
#       o __radd__ : nova data igual a dias (int) + data
#       o __sub__  : dias (int) que resultam de data - data
#       * NOTA: usar módulo datetime para fazer as contas com datas

class InvalidDateValues(ValueError):
    pass

