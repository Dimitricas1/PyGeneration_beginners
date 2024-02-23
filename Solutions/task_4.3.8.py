a = int(input())
b = int(input())
operator = input()

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("На ноль делить нельзя!")
else:
    print("Неверная операция")
