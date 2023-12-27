def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def montgomery_add(P, Q):
    if P == Q:
        return montgomery_double(P)
    
    x1, y1 = P
    x2, y2 = Q
    
    alpha = ((y2 - y1) * modinv(x2 - x1, p)) % p
    x3 = (B * alpha ** 2 - A - x1 - x2) % p
    y3 = (alpha * (x1 - x3) - y1) % p
    
    return (x3, y3)

def montgomery_double(P):
    x1, y1 = P
    
    alpha = ((3 * x1 ** 2 + 2 * A * x1 + 1) * modinv(2 * B * y1, p)) % p
    x3 = (B * alpha ** 2 - A - 2 * x1) % p
    y3 = (alpha * (x1 - x3) - y1) % p
    
    return (x3, y3)

def montgomery_ladder(k, G_x):
    P = (G_x, 1)  # Initial point P
    Q = (2 * G_x % p, (G_x ** 3 + A * G_x ** 2 + G_x) % p)  # Initial point [2]P
    
    for bit in reversed(format(k, 'b')[:-1]):  # Skip the first bit since it's always 1
        if bit == '0':
            P, Q = montgomery_double(P), montgomery_add(P, Q)
        else:
            P, Q = montgomery_add(P, Q), montgomery_double(Q)
    
    return P

# Scalar multiplication for Q = [0x1337c0decafe] * G
p = 2255 - 19
A = 486662
B = 1
G_x = 9

k = 0x1337c0decafe
Q_x = montgomery_ladder(k, G_x)[0]

print("crypto{" + hex(Q_x)[2:] + "}")
