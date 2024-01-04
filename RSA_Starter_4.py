from sympy import mod_inverse

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

phi_N = (p - 1) * (q - 1)

d = mod_inverse(e, phi_N)
print(d)
