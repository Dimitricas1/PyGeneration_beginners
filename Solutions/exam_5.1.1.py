year = int(input())

if (year // 10**0) % 10 == 0 and (year // 10**1) % 10 == 0:
    print("YES")
else:
    print("NO")
