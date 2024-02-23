color_a = input()
color_b = input()

red = "красный"
cyan = "синий"
yellow = "желтый"
purple = "фиолетовый"
orange = "оранжевый"
green = "зеленый"

# Сразу отсеиваем варианты с ошибочным вводом
if color_a not in (red, cyan, yellow) or color_b not in (red, cyan, yellow):
    print("ошибка цвета")
elif color_a == color_b:
    print(color_a)
elif red in (color_a, color_b):
    if cyan in (color_a, color_b):
        print(purple)
    elif yellow in (color_a, color_b):
        print(orange)
else:
    print(green)
