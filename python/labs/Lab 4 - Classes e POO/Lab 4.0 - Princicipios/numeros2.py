import math

class Rational:

    def __init__(self, numer: int, denom: int):
        if denom == 0:
            raise ValueError('math domain error')        
        gcd = math.gcd(numer, denom)
        self._n = numer // gcd
        self._d = denom // gcd
        # self.pair = [numer // gcd, denom // gcd]

    @classmethod
    def from_str(cls, string: str) -> 'Rational': 
        r = string.split('/')  
        return cls(int(r[0].strip()), int(r[1].strip()))

    def get_numer(self) -> int:   # getters
        return self._n
        # return self.pair[0]

    # def set_numer(self, new_numer: int):
    #     gcd = math.gcd(new_numer, self.d)
    #     self._n = new_numer // gcd
    #     self._d = self.d // gcd
    # #     gcd = math.gcd(new_numer, self._par[1])
    # #     self._par[0] = new_numer // gcd
    # #     self._par[1] = self._par[1] // gcd



    def get_denom(self) -> int:
        return self._d

    def add(self, r: 'Rational') -> 'Rational':
        return Rational(self.get_numer() * r.get_denom() + r.get_numer() * self.get_denom(), self.get_denom() * r.get_denom())

    def sub(self, r: 'Rational') -> 'Rational':
        return Rational(self.get_numer() * r.get_denom() - r.get_numer() * self.get_denom(), self.get_denom() * r.get_denom())        

    def mul(self, r: 'Rational') -> 'Rational':
        return Rational(self.get_numer() * r.get_numer(), self.get_denom() * r.get_denom())        

    def div(self, r: 'Rational') -> 'Rational':
        return Rational(self.get_numer() * r.get_denom(), self.get_denom() * r.get_numer())        

    def pow(self, exp) -> 'Rational':
        r = self if exp >= 0 else self.invert()
        return Rational(r.numer ** abs(exp), r.denom ** abs(exp))

    def eq(self, r: 'Rational') -> bool:
        return self.get_numer() * r.get_denom() == self.get_denom() * r.get_numer()

    def neq(self, r: 'Rational') -> bool:
        return not self.eq(r)

    def gt(self, r: 'Rational') -> bool:
        return self.get_numer() * r.get_denom() > self.get_denom() * r.get_numer()
    
    def ge(self, r: 'Rational') -> bool:
        return self.gt(r) or self.eq(r)

    def lt(self, r: 'Rational') -> bool:
        return not self.ge(r)

    def le(self, r: 'Rational') -> bool:
        return not self.gt(r)

    def invert(self) -> 'Rational':
        return Rational(self.get_denom(), self.get_numer())

   
    def to_str(self) -> str:
        return f'{self.get_numer()}/{self.get_denom()}'

    
r1 = Rational(1, 2)
r2 = Rational(1, 4)
r3 = r1.add(r2)
print(r1.get_numer(), r1.get_denom())


class Complex:
    """
    Representação de um número complexo na forma rectangular.
    """

    def __init__(self, real: float, imag: float):
        self._real = real
        self._imag = imag

    @classmethod
    def from_mag_angle(cls, mag: float, angle: float): 
        return cls(mag*math.cos(angle), mag*math.sin(angle))

    @classmethod
    def from_real_imag(cls, real: float, imag: float): 
        return cls(real, imag)

    def get_real_part(self) -> float:
        return self._real

    def get_imag_part(self) -> float:
        return self._imag

    def get_magnitude(self) -> float:
        r, i = self.get_real_part(), self.get_imag_part()
        return math.sqrt(r**2 + i**2)

    def get_angle(self) -> float:
        r, i = self.get_real_part(), self.get_imag_part()
        return math.atan2(i, r)

    def add(self, c: 'Complex') -> 'Complex':
        return Complex.from_real_imag(
            self.get_real_part() + c.get_real_part(),
            self.get_imag_part() + c.get_imag_part(),
        )

    def mul(self, c: 'Complex') -> 'Complex':
        return Complex.from_mag_angle(
            self.get_magnitude() * c.get_magnitude(),
            self.get_angle() + c.get_angle(),
        )

    def to_str(self) -> str:
        return f'{self.get_real_part():.1f}+{self.get_imag_part():.1f}i'

c1 = Complex(1, 3)
c2 = Complex.from_real_imag(1, 3)
c3 = Complex.from_mag_angle(1, math.pi/4)
print(c1.to_str())  
print(c2.to_str())
print(c3.to_str())

c4 = c1.add(c2)


L = [(r1, r2), (c1, c2)]
for x, y in L:
    print(x.to_str(), '+', y.to_str(), '=', x.add(y).to_str())

