summ = int(input())
counter = 0

while summ != 0:
    if summ // 25 >= 1:
        summ -= 25
        counter += 1
    elif summ // 10 >= 1:
        summ -= 10
        counter += 1
    elif summ // 5 >= 1:
        summ -= 5
        counter += 1
    else:
        counter += summ
        summ = 0

print(counter)
