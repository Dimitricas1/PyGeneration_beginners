number = int(input())

a = (number // 10**2) % 10
b = (number // 10**1) % 10
c = (number // 10**0) % 10

maximum = max(a, b, c)
minimum = min(a, b, c)
middle = a + b + c - maximum - minimum

if maximum - minimum == middle:
    print("Число интересное")
else:
    print("Число неинтересное")
