
v = (2, 6, 3)
w = (1, 0, 0)
u = (7, 7, 2)

vector_1 = (2 * v[0] - w[0], 2 * v[1] - w[1], 2 * v[2] - w[2])


vector_2 = (3 * vector_1[0], 3 * vector_1[1], 3 * vector_1[2])


result = vector_2[0] * 2 * u[0] + vector_2[1] * 2 * u[1] + vector_2[2] * 2 * u[2]


print("The result of the expression is:", result)
