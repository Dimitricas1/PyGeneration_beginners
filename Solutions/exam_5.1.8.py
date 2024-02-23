ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())

if (ax - bx) ** 2 == (ay - by) ** 2 or ax == bx or ay == by:
    print("YES")
else:
    print("NO")
