mx = -1000000
s = 0
flag = False
for _ in range(10):
    x = int(input())
    if x < 0:
        flag = True
        s += x
        if x > mx:
            mx = x
if flag:
    print(s)
    print(mx)
else:
    print("NO")
