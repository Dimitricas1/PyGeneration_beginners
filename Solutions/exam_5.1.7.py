ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())

if (ax - bx) ** 2 == 4:
    if (ay - by) ** 2 == 1:
        print("YES")
    else:
        print("NO")
elif (ax - bx) ** 2 == 1:
    if (ay - by) ** 2 == 4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
