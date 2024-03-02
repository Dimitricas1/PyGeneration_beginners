len_1 = len(input())
len_2 = len(input())
len_3 = len(input())

if len_2 > len_3:
    len_3, len_2 = len_2, len_3

if len_1 > len_2:
    len_2, len_1 = len_1, len_2

if len_2 > len_3:
    len_3, len_2 = len_2, len_3

if len_3 - len_2 == len_2 - len_1:
    print("YES")
else:
    print("NO")
