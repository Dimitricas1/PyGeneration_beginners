digit = int(input())

thousands = (digit // 10**3) % 10
hundreds = (digit // 10**2) % 10
decimals = (digit // 10**1) % 10
units = (digit // 10**0) % 10

if thousands + units == hundreds - decimals:
    print("ДА")
else:
    print("НЕТ")
