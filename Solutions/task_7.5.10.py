number = int(input())
flag = True
curr_digit = number % 10

while number > 0:
    if curr_digit > number % 10:
        flag = False
    curr_digit = number % 10
    number //= 10

print("YES" if flag else "NO")
