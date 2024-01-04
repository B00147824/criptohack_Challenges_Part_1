message = 12
e = 65537
p = 17
q = 23

N = p * q
ciphertext = pow(message, e, N)

print(ciphertext)