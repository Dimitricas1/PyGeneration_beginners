ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())

if (ax - bx) % 2 == 0:
    if (ay - by) % 2 == 0 or ay == by:
        print("YES")
    else:
        print("NO")
else:
    if (ay - by) % 2 != 0 and ay != by:
        print("YES")
    else:
        print("NO")
