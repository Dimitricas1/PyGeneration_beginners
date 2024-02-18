number = int(input())

hundreds = (number // 10**2) % 10
decimals = (number // 10**1) % 10
units = (number // 10**0) % 10

print(hundreds, decimals, units, sep="")
print(hundreds, units, decimals, sep="")
print(decimals, hundreds, units, sep="")
print(decimals, units, hundreds, sep="")
print(units, hundreds, decimals, sep="")
print(units, decimals, hundreds, sep="")
