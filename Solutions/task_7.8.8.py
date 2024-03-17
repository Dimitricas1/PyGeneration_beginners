n = int(input())

for i in range(1, n + 1):
    for _ in range(min((i, n + 1 - i))):
        print("*", end="")
    print()
