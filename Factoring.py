from sympy import factorint

# Given 150-bit number
modulus = 510143758735509025530880200653196460532653147

# Factorize the modulus to find its prime factors
factors = factorint(modulus)

# Extract the two prime factors
prime_factors = list(factors.keys())

# Print the smaller prime factor
print("Smaller prime factor:", min(prime_factors))
