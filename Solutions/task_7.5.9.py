number = int(input())
same_digits = True
digit = number % 10

while number > 0:
    if number % 10 != digit:
        same_digits = False
    number //= 10

print("YES" if same_digits else "NO")
