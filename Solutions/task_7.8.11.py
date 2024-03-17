for n in range(1, 11):
    for k in range(1, 11):
        for m in range(1, 10):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n, k, m, sep=", ")
