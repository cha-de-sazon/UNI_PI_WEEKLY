# Sejam A e B dois pontos quaisquer no plano cartesiano, representados por um par de coordenadas (x, y). 
# A menor distância entre A e B é um segmento de reta que tem os dois pontos como extremidade. 
# Representando as coordenadas de A pelo par(Ax, Ay), e as coordenadas de B pelo par (Bx, By)

import math

def distancia(ax, ay, bx, by):
    return(math.sqrt(pow((bx - ax), 2) + pow((by - ay), 2)))

a = int(input())
a = int(input())
b = int(input())
b = int(input())

print(f"{distancia(a, a, b, b):.2f}")