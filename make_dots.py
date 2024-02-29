# v=H*r = ds/s0(Z) * c
# H * r = Z * c

"""
H : 60 ~ 80 사이
r : 십의 자리에서 천의자리 : 1500까지는 가능  = 거리
v : 당연히 높은 숫자가 나오는게 당연한거 아님?
Z : v/c
"""

right_angle_portion = [
    [3, 4, 5],
    [5, 12, 13],
    [8, 15, 17]
]
c = 300000

import random
from fractions import Fraction
import math
from math import sqrt
from copy import deepcopy
"""
두 천체 사이의 거리
1. 허블상수는 60~80 사이의 자연수일 것(70, 75) -> random 하면 되겠죠
2. c = 300000
3. H, Z를 적당한 숫자로 만들어야되고,
4. 그랬을때 v가 적당한 숫자가 나와야한다.
"""

def make_H():
    mylist = [60, 65, 70, 75, 80]
    return random.choice(mylist)

def make_v_r(H):
    semi_r = random.randint(1, 9)
    semi_r_2 =  random.randint(0, 2)
    r = semi_r * pow(10, semi_r_2)
    v = H * r
    return v, r

def make_Z(v):
    return Fraction(v, 300000)

def decide_two_dot():
    H = make_H()
    v, r = make_v_r(H)
    Z = make_Z(v)
    return H, v, r, Z

"""
두 천체 사이의 거리
1. 허블상수는 60~80 사이의 자연수일 것(70, 75) -> random 하면 되겠죠
2. c = 300000
3. H, Z를 적당한 숫자로 만들어야되고,
4. 그랬을때 v가 적당한 숫자가 나와야한다.
"""

def decide_portion():
    a = deepcopy(random.choice(right_angle_portion))
    return a

def make_v(H, r):
    v = H * r
    return v

def decide_three_dot_right_integer():
    portion = decide_portion()
    semi_r = random.randint(1, 9)
    semi_r_2 =  random.randint(0, 1)
    spec_num = semi_r * pow(10, semi_r_2)
    for i in range(len(portion)):
        portion[i] *= spec_num

    H = make_H()
    v1 = make_v(H, portion[0])
    v2 = make_v(H, portion[1])
    v3 = make_v(H, portion[2])
    Z1 = make_Z(v1)
    Z2 = make_Z(v2)
    Z3 = make_Z(v3)

    return [H, v1, portion[0], Z1], [H, v2, portion[1], Z2], [H, v3, portion[2], Z3]


for i in range(10):
    print(decide_three_dot_right_integer())


"""


class SquareRoot:
    def __init__(self, value):
        if value < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        self.value = value

    def __repr__(self):
        return f"SquareRoot({self.value})"

    def __str__(self):
        return f"√{self.value}"

    def __add__(self, other):
        if not isinstance(other, SquareRoot):
            raise TypeError("Unsupported operand type. Please use SquareRoot instances.")
        return SquareRoot(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, SquareRoot):
            raise TypeError("Unsupported operand type. Please use SquareRoot instances.")
        if self.value - other.value < 0:
            raise ValueError("Resulting square root is negative.")
        return SquareRoot(self.value - other.value)

    # You can implement other arithmetic operations as needed

# Example usage:
root1 = SquareRoot(9)
root2 = SquareRoot(16)

print(root1)  # Output: √9
print(root2)  # Output: √16

result = root1 + root2
print(result)  # Output: √25

result = root2 - root1
print(result)  # Output: √7

"""
