def is_primitive_element(g, p):
    # Check if g is a primitive element modulo p
    for i in range(2, p - 1):
        if pow(g, i, p) == 1:
            return False
    return True

def find_primitive_element(p):
    # Find the smallest primitive element modulo p
    for g in range(2, p):
        if is_primitive_element(g, p):
            return g

p = 28151
primitive_element = find_primitive_element(p)

print("Smallest primitive element modulo", p, ":", primitive_element)
