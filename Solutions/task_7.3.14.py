flag = True

for _ in range(10):
    number = int(input())
    if number % 2 != 0:
        flag = False

print("YES" if flag else "NO")
