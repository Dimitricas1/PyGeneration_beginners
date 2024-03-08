m = int(input())
n = int(input())

# Если число кратно 3 и кратно 5, то оно кратно 15
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)
