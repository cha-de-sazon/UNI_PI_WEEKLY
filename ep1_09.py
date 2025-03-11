a = int(500)
b = int(100)
c = int(25)
d = int(1)

carga = int(input(":"))
pesos = [a, b, c, d]

caixas1 = [carga // peso for peso in pesos]

caixas = [caixas1[0], caixas1[1] - (5 * caixas1[0]), caixas1[2] - (4 * caixas1[1]), caixas1[3] - (25 * caixas1[2])]

print(caixas)
