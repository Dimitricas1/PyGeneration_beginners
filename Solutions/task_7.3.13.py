n = int(input())
largest_1 = 0
largest_2 = 0

for _ in range(n):
    number = int(input())
    if number > largest_1:
        largest_2 = largest_1
        largest_1 = number
    elif number > largest_2:
        largest_2 = number

print(largest_1)
print(largest_2)
