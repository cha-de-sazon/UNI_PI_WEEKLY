import math

def distancia(ax, ay, bx, by):
    return(math.sqrt(pow((bx - ax), 2) + pow((by - ay), 2)))

a = int(input())
a = int(input())
b = int(input())
b = int(input())

print(f"{distancia(a, a, b, b):.2f}")
