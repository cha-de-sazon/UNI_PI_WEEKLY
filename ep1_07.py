d1 = 10
d2 = 10
t1 = float(input())

def desconto(t, d1, d2):
    td = float(t - (t * (d1/100)))
    vf = float(td - (td * (d2/100)))
    return(vf)

print(desconto(t1, d1, d2))
