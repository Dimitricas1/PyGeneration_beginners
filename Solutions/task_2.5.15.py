number = int(input())

hundreds = number // 100
decimals = number // 10 % 10
units = number % 10

print("Сумма цифр =", hundreds + decimals + units)
print("Произведение цифр =", hundreds * decimals * units)
