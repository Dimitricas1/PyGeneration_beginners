month = int(input())

if month == 2:
    print(28)
else:
    # С 1 по 7 месяц в нечётных месяцах 31 день, с 8 по 12 - наоборот, поэтому
    # если попадается с 1 по 7 месяц, добавляем 1
    if month <= 7:
        month += 1
    if month % 2 == 0:
        print(31)
    else:
        print(30)
