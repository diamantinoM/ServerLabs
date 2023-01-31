"""
LABORATÓRIO 4 

Exemplos, e respectiva teoria, a respeito de alguns dos conceitos 
que estão na base da Programação Orientada por Objectos (POO).

https://docs.python.org/3/reference/datamodel.html
https://docs.python.org/3/library/functools.html#functools.total_ordering
"""

import math
from functools import total_ordering
from abc import ABC, abstractmethod


@total_ordering
class Rational:

    def __init__(self, n: int, d: int) -> None:
        if d == 0:
            raise ValueError("math domain error")
        g = math.gcd(n, d)
        self._n = n // g
        self._d = d // g

    @classmethod
    def from_str(cls, string: str) -> 'Rational': 
        r = string.split('/')  
        return cls(int(r[0].strip()), int(r[1].strip()))

    @property
    def numer(self):
        return self._n

    @property
    def denom(self):
        return self._d

    def __add__(self, r: 'Rational') -> 'Rational':
        return Rational(
            self.numer *r.denom + r.numer*self.denom, 
            self.denom*r.denom
        )

    def __sub__(self, r: 'Rational') -> 'Rational':
        return Rational(
            self.numer * r.denom - r.numer * self.denom, 
            self.denom * r.denom
        )

    def __mul__(self, r: 'Rational') -> 'Rational':
        return Rational(self.numer * r.numer, self.denom * r.denom)

    def __truediv__(self, r: 'Rational') -> 'Rational':
        return Rational(self.numer * r.denom, self.denom * r.numer)        

    def __pow__(self, e: int) -> 'Rational':
        return Rational(self.numer ** e, self.denom ** e)
    
    # r1 == r2  =>   r1.__eq__(r2) 
    def __eq__(self, r: object) -> bool:
        if self.__class__ is r.__class__:
            return self.numer * r.denom == self.denom * r.numer
        return NotImplemented

    def __gt__(self, r: 'Rational') -> bool:
        return self.numer * r.denom > self.denom * r.numer

    # def __radd__(self, r: 'Rational') -> 'Rational':
    #     return self if r == 0 else self + r

    def __repr__(self):
        return f'{str(self.__class__.__name__)}({self.numer}, {self.denom})'

    def __str__(self):
        return f'{self.numer}/{self.denom}'


class Complex(ABC):
    """
    Representação abstracta de um número complexo.
    """

    @property
    @abstractmethod
    def real_part(self):
        pass

    @property
    @abstractmethod
    def imag_part(self):
        pass

    @property
    @abstractmethod
    def magnitude(self):
        pass

    @property
    @abstractmethod
    def angle(self):
        pass

    @classmethod
    @abstractmethod
    def from_real_imag(cls, real: float, imag: float):
        pass

    @classmethod
    @abstractmethod
    def from_mag_angle(cls, mag: float, angle: int):
        pass

    def __add__(self, z: 'Complex') -> 'Complex':
        return self.from_real_imag(
            self.real_part + z.real_part,
            self.imag_part + z.imag_part
        )

    def __sub__(self, z: 'Complex') -> 'Complex':
        return self.from_real_imag(
            self.real_part - z.real_part,
            self.imag_part - z.imag_part
        )

    def __mul__(self, z: 'Complex') -> 'Complex':
        return self.from_mag_angle(
            self.magnitude * z.magnitude,
            self.angle + z.angle
        )

    def __truediv__(self, z: 'Complex') -> 'Complex':
        return self.from_mag_angle(
            self.magnitude / z.magnitude,
            self.angle - z.angle
        )

    def __pow__(self, e: float) -> 'Complex': 
        return self.from_mag_angle(self.magnitude ** e, e * self.angle)

    def __eq__(self, z: 'Complex') -> bool:
        if self.__class__ is Complex and z.__class__ is Complex:
            return self.real_part == z.real_part and self.imag_part == z.imag_part
        return NotImplemented

    def __ne__(self, z: 'Complex') -> bool:
        if self.__class__ is z.__class__:
            return not self == z
        return NotImplemented

    @abstractmethod
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        pass


class ComplexRectang(Complex):
    """
    Representação de um número complexo na forma rectangular.
    """

    def __init__(self, real: float, imag: float):
        self._real = real
        self._imag = imag

    @classmethod
    def from_real_imag(cls, real: float, imag: float): 
        return cls(real, imag)

    @classmethod
    def from_mag_angle(cls, mag: float, angle: float): 
        return cls(mag*math.cos(angle), mag*math.sin(angle))

    @property
    def real_part(self) -> float:
        return self._real

    @property
    def imag_part(self) -> float:
        return self._imag

    @property
    def magnitude(self) -> float:
        r, i = self.real_part, self.imag_part
        return math.sqrt(r**2 + i**2)

    @property
    def angle(self) -> float:
        r, i = self.real_part, self.imag_part
        return math.atan2(i, r)

    def __str__(self) -> str:
        return f'{self.real_part:.1f}+{self.imag_part:.1f}i'

    def __repr__(self) -> str:
        const_name = ComplexRectang.from_real_imag.__qualname__
        return f'{const_name}({self.real_part:.1f}, {self.imag_part:.1f})'



