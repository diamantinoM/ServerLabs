

from typing import Union
from decimal import Decimal
from enum import Enum


class Vehicle:    # class Vehicle(object)
    def __init__(
            self,
            make: str,
            model: str,
            mileage: int,
            price: Union[str, Decimal]
    ):
        if mileage < 0:
            raise ValueError("Invalid mileage", mileage)
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = Decimal(price) 

    # Vehicle: make=Ford, model=Fiesta, mileage=10000, price=10000
    def __str__(self):
        cls_name = self.__class__.__name__
        txt = '{}: make={}, model={}, mileage={}, price={}'
        return txt.format(
            cls_name, 
            self.make, 
            self.model, 
            self.mileage, 
            self.price,
        )

    def __repr__(self):
        attrs = vars(self)
        attrs_txt = []
        for attr_name, attr_val in attrs.items():
            attrs_txt.append('{}={}'.format(attr_name, repr(attr_val)))
        return '{}({})'.format(self.__class__   .__name__, ','.join(attrs_txt))


class Car(Vehicle):
    def __init__(self, doors: int, *args, **kargs):
        if doors not in (2, 4):
            raise ValueError("Invalid number of doors")
        super().__init__(*args, **kargs)
        self.doors = doors


DriveType = Enum('DriveType', 'TWO_WHEEL FOUR_WHEEL SIX_WHEEL')


class Truck(Vehicle):
    def __init__(self, drive: DriveType, *args, **kargs):
        super().__init__(*args, **kargs)
        self.drive = drive

    def __str__(self):
        txt = super().__str__()
        return txt + ', drive=' + str(self.drive)



car1 = Car(
    doors=2,
    make='Ford',
    model='Fiesta',
    mileage=100000,
    price='1730.43',
)


truck1 = Truck(
    drive=DriveType.FOUR_WHEEL,
    make='Ford',
    model='F150',
    mileage=1000000,
    price='20000',
)



# def f(x, y, z=32):
#     print('F', x, y, z)


# def g(a, b=80):
#     print('G', a, b)


# def h(p, *args, **kargs):
#     if p == 1:
#         f(*args, **kargs)
#     elif p == 2:
#         g(*args, **kargs)
