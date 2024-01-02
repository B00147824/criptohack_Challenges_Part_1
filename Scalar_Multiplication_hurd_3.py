from Crypto.Util.number import inverse
a = 497
b = 1768
p = 9739

P = (2339, 2213)
def point_addition(P, Q):
      O = (0, 0)
    if P == O:
        return Q
    if Q == O:
        return P   
    x1, y1 = P[0], P[1]
    x2, y2 = Q[0], Q[1]
      if x1 == x2 and y1 == -y2:
        return O
    if P != Q:
        lam = ((y2 - y1) * inverse(x2 - x1, p)) % p
      else:
        lam = ((3 * x1**2 + a) * inverse(2 * y1, p)) % p
    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    summation = (x3, y3)
    return summation
def scalar_multiplication(n, P):
    O = (0, 0)
    Q, R = P, O
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q)
        Q = point_addition(Q, Q)
        n //= 2
    return R
print(scalar_multiplication(7863, P))#!/usr/bin/env python3
from Crypto.Util.number import inverse
a = 497
b = 1768
p = 9739
P = (2339, 2213)
def point_addition(P, Q):
    O = (0, 0)
    if P == O:
        return Q 
    if Q == O:
        return P
    x1, y1 = P[0], P[1]
    x2, y2 = Q[0], Q[1]
    if x1 == x2 and y1 == -y2:
        return O
    if P != Q:
        lam = ((y2 - y1) * inverse(x2 - x1, p)) % p
    else:
        lam = ((3 * x1**2 + a) * inverse(2 * y1, p)) % p
    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    summation = (x3, y3)
    return summation
def scalar_multiplication(n, P):
    O = (0, 0)
    Q, R = P, O
    while n > 0:
        if n % 2 == 1:
            R = point_addition(R, Q)
        Q = point_addition(Q, Q)
        n //= 2
    return R
print(scalar_multiplication(7863, P))
