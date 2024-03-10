number = int(input())
summ = 0
count = 0
multipl = 1
first_digit = 0
last_digit = number % 10

while number != 0:
    digit = number % 10
    summ += digit
    multipl *= digit
    count += 1
    if number < 10:
        first_digit = number
    number //= 10

print(summ)
print(count)
print(multipl)
print(summ / count)
print(first_digit)
print(first_digit + last_digit)
