n = int(input())
max_digit = 0
flag = False
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        flag = True
        if digit > max_digit:
            max_digit = digit
    n //= 10
print(max_digit if flag else "NO")
