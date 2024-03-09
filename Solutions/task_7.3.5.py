a = int(input())
b = int(input())
count = 0

for i in range(a, b + 1):
    cube = i * i * i
    if cube % 10 == 4 or cube % 10 == 9:
        count += 1
print(count)
