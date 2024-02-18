num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

# Примем первое число за наименьшее
minimal = num_1

if num_2 < minimal:
    minimal = num_2

if num_3 < minimal:
    minimal = num_3

if num_4 < minimal:
    minimal = num_4

print(minimal)
