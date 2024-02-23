a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равносторонний")
elif a in (b, c) or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")
