n = int(input())
count = 0

for i in range(1, n + 1):
    square = i * i
    if square % 10 in (2, 5, 8):
        count += i
print(count)
