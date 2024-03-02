city_1 = input()
city_2 = input()
city_3 = input()

len_city_1 = len(city_1)
len_city_2 = len(city_2)
len_city_3 = len(city_3)

shortest_city = ""
longest_city = ""

for city in (city_1, city_2, city_3):
    if len(city) == min(len_city_1, len_city_2, len_city_3):
        shortest_city = city
    elif len(city) == max(len_city_1, len_city_2, len_city_3):
        longest_city = city

print(shortest_city)
print(longest_city)
