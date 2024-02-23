section = int(input())

if section == 0:
    print("зеленый")
elif 1 <= section <= 10 or 19 <= section <= 28:
    if section % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 11 <= section <= 18 or 29 <= section <= 36:
    if section % 2 == 0:
        print("красный")
    else:
        print("черный")
else:
    print("ошибка ввода")
