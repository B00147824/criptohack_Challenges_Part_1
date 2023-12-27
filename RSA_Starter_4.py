from sympy import mod_inverse

# Given values
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Calculate the totient (phi) of N
phi_N = (p - 1) * (q - 1)

# Calculate the private key (d)
d = mod_inverse(e, phi_N)

# Print the result
print(d)
