# Import necessary module
from Crypto.Cipher import AES
from Crypto.Util.number import inverse
from Crypto.Util.Padding import pad, unpad
from collections import namedtuple
from random import randint
import hashlib
import os

# Create a simple Point class to represent the affine points.
Point = namedtuple("Point", "x y")

# The point at infinity (origin for the group law).
O = 'Origin'

# Define the curve parameters
p = 310717010502520989590157367261876774703
a = 2
b = 3

# ... (other functions and code) ...

def double_and_add(P: tuple, n: int):
    # based on the algorithm in ICM
    Q = P
    R = O
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q)
        Q = point_addition(Q, Q)
        n = n // 2
    assert check_point(R)
    return R

# ... (rest of the code) ...
