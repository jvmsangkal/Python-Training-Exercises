def multiplication_table(n, m):
    return [[i * j for i in range(1, n + 1)] for j in range(1, m + 1)]


print(multiplication_table(3, 4))
