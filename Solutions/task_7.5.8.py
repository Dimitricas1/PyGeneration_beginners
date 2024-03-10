number = int(input())
second_digit = 0

while number > 9:
    second_digit = number % 10
    number //= 10
print(second_digit)
