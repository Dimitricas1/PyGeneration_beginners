number = int(input())

largest = smallest = number % 10

while number != 0:
    digit = number % 10
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    number //= 10

print("Максимальная цифра равна", largest)
print("Минимальная цифра равна", smallest)
