# Exercício: Exercite a formatação de saídas. Seu programa irá receber 3 valores, 
# então deverá imprimir o primeiro formatado com nenhuma casa decimal, 
# o segundo com duas casas e o terceiro com três casas

# input 1 = 2
# input 2 = 1.41421
# input 3 = 3.14159

n1 = int(input())
print(f"Primeiro numero = {n1}")

n2 = float(input())
print(f"{n2:.2f} eh o segundo numero")

n3 = float(input())
print(f"Finalmente {n3:.3f} eh o terceiro numero")