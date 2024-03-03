from math import cos, pow, radians, sin, tan

x = float(input())

rads = radians(x)

print(sin(rads) + cos(rads) + pow(tan(rads), 2))
