import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
r = []

d = pow(b, 2) - (4 * a * c)

if d < 0:
    print("Sem solucao real!")
    print(f"Delta = {d:.2f}")
else:
    d1 = math.sqrt(d)    
    x1 = ((-b) + d1) / (2 * a)
    x2 = ((-b) - d1) / (2 * a)
    if d == 0:
        r = [x1]
        print(f"x = {r[0]:.2f}")
    else:
        r = [x1, x2]
        r.sort()
        print(f"x1 = {r[0]:.2f}")
        print(f"x2 = {r[1]:.2f}")