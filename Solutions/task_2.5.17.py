number = int(input())

thousands = (number // 10**3) % 10
hundreds = (number // 10**2) % 10
decimals = (number // 10**1) % 10
units = (number // 10**0) % 10

print("Цифра в позиции тысяч равна", thousands)
print("Цифра в позиции сотен равна", hundreds)
print("Цифра в позиции десятков равна", decimals)
print("Цифра в позиции единиц равна", units)
