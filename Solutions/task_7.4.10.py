total = 0
text = input()

while text != "стоп" and text != "хватит" and text != "достаточно":
    total += 1
    text = input()

print(total)
