sal = float(input("Salário: "))
ven = float(input("Vendas: "))
com = 20

pco = ven * (com / 100)
tot = sal + pco

print(f"{pco:.2f}")

if pco >= (sal / 2):
    print("Atingiu meta de vendas")
else:
    print("Nao atingiu meta de vendas")