from math import ceil

m = int(input())
n = int(input())

m = 2 * ceil(m / 2) - 1

for i in range(m, n - 1, -2):
    print(i)
