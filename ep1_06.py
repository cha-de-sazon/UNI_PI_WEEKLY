a1 = int(input())
r = int(input())
n = int(input())

def somapa(a1, r, n):
    return(n * (a1 + (a1 + (n - 1) * r)) / 2)
    
print(somapa(a1, r, n))
