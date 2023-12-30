from Crypto.Cipher import AES
from Crypto.Util.number import inverse
from Crypto.Util.Padding import pad, unpad
from collections import namedtuple
from random import randint
import hashlib
import os
Point = namedtuple("Point", "x y")
O = 'Origin'

p = 310717010502520989590157367261876774703
a = 2
b = 3

def double_and_add(P: tuple, n: int): 
    Q = P
    R = O
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q)
        Q = point_addition(Q, Q)
        n = n // 2
    assert check_point(R)
    return R


