a = int(input())
b = int(input())
c = int(input())

maximum = max(a, b, c)
middle = min(max(a, b), max(b, c), max(a, c))
minimum = min(a, b, c)

print(maximum)
print(middle)
print(minimum)
