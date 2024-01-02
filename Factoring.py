from sympy import factorint

modulus = 510143758735509025530880200653196460532653147
factors = factorint(modulus)

prime_factors = list(factors.keys())
print("Smalle factor prime:", min(prime_factors))
